-- 입사일의 마지막 날짜를 출력하시오
--last_day
select last_day(hire_date) from employees;

--가입일 1년후
select add_months(sdate,12) from students;
select add_months(sdate,-6) from students;

--현재일 기준 가입일 6개월 이내의 회원
select name,sdate from students
where sdate>=add_months(sysdate,-6)
order by sdate;

--년도 월별로 가입인원을 출력
select mdate,last_day(mdate) from member;

select name, mdate,last_day(mdate) md from member
order by md;

select substr(last_day(mdate),1,5) md, count(*) from member
GROUP by last_day(mdate) order by md;

-- 부서별 일원을 출력하시오
select department_id,count(*) from employees
group by department_id
;

--테이블 복사
drop table emp3;
create table emp3 as select * from employees;
--구조만 복사
create table emp4 as select * from employees where 1=2;

select * from emp4;
--테이블 구조가 있는상태에서 모든 데이터를 입력하는 방법
insert into emp4 select * from employees;

rollback;
-- 제약조건을 확인
insert into emp4(employee_id,emp_name,hire_date)
select employee_id,emp_name,hire_date from employees;

----- 테이블
--create: 생성 alter 변경 drop 삭제

select * from emp4;
--alter add: 테이블에 컬럼추가
alter table emp4
add(hire_date2 date);

desc emp4;

--컬럼변경: 컬럼안에 데이터가 있다면 제약조건( 65 길이의 문자가 있을경우 50으로 변경안됨)
alter table emp4
modify(email varchar2(70));

alter table emp4
modify(email varchar2(50));

select emp_name from emp4;
desc emp4;
alter table emp4
modify(emp_name varchar2(20));
--컬럼의 길이 확인
select max(length(emp_name)) from employees;
select length(emp_name) em from employees
order by em desc;

--컬럼 형태 변경 > 컬럼 안 데이터가 null 일때 가능
--다른 타입인 경우 데이터를 null로 변경한 후 타입을 변경해야한다
select * from emp4;
alter table emp4
modify(email number(6));
--다른 타입
alter table emp4 
modify(emp_name number(20));

desc emp4;

-- employee_id값을 email 컬럼에 복사
update emp4 set email = employee_id;
-- employee_id(숫자형타입)값을 phone_number(문자형타입) 입력
update emp4 set phone_number = employee_id;
commit;
rollback;
-- 문자형타입을 숫자형 타입에 복사
-- 안에 있는 데이터가 모두숫자형이기에 가능
-- 문자가 포함되어있으면 타입변경이 불가
update emp4 set phone_number = '198a' where employee_id=198;
update emp4 set manager_id = phone_number;

select * from emp4;
--컬럼 이름변경
desc emp4;
alter table emp4 rename column phone_number to p_number;

--속성 변경가능
alter table emp4 modify hire_date date null; -- modify 괄호안해도 됨
alter table emp4 modify hire_date date not null;

--컬럼 삭제
alter table emp4
drop column hire_date2;
desc emp4;

--테이블 삭제
drop table emp2;
drop table emp3;

--테이블 이름변경
rename emp4 to emp44;

----
select * from departments;
-------
drop table board;
--primary key 중복불가,null값 불가
--unique 중복불가,null값 허용
--not null 중복가능,null값 불가 
-- default 값이 입력되지 않았을때 디폴트값 지정


create table bmember(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30)not null,
nicname varchar2(30),
age number(3) default 0,
gender varchar2(6) check(gender in('Male','Female')),
--check - Male,Female 2가지 형태외에는 입력이 안됨
-- 소문자 대문자 바뀌어도 안됨
email varchar2(20),
bdate date default sysdate
);

desc bmember;
drop table bmember;

insert into bmember(id,pw,name,nicname,age,gender,email,bdate)values(
'aaa','1111','홍길동','길동스',20,'Male','aaa@aaa.com',sysdate);

insert into bmember(id,pw,name,nicname,gender,email)values(
'bbb','2222','유관순','관순스','Female','bbb@bbb.com');

select * from bmember;

--not null null 허용하지않음 빈공백은 가능함
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
'aaa','1111','홍길동','길동스',20,'Male','aaa@aaa.com',2024/01/01);

--primary key 중복불가,null값 불가
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
'aaa','1111','홍길동','길동스',20,'Male','aaa@aaa.com',2024/02/01);


create table emp3(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp3 values(
1,'홍','01','01'
);

insert into emp3 values(
2,'홍','02','02'
);
--unique null값은 허용
insert into emp3(ename,job,deptno)values(
'이','01','01'
);
-- unique 중복은불가
insert into emp3 values(
2,'강','04','04'
);



select * from member;

--primary key 등록: 중복불가 null불가
insert into member values(
'fff','1111','홍길w자','aaa@aaa.com','123-456-7890','Female','golf',sysdate
);
commit;
--primary key 등록: 중복불가 null불가
-- primary key 추가,수정
-- constraint id_pk :이름설정
alter table member add constraint id_pk primary key (id);

--primary key 삭제
alter table member drop constraint id_pk;

alter table member add constraint id_pk primary key (id);


desc bmember;

create table board(
bno number(4) primary key,
btitle varchar2(100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile varchar2(100)
);

insert into board values(
BOARD_SEQ.nextval,'제목1','내용1','aaa',BOARD_SEQ.currval,0,0,0,sysdate,''
);
insert into board values(
BOARD_SEQ.nextval,'제목2','내용2','bbb',BOARD_SEQ.currval,0,0,0,sysdate,''
);
insert into board values(
BOARD_SEQ.nextval,'제목5','내용5','ddd',BOARD_SEQ.currval,0,0,0,sysdate,''
);

commit;

select * from board;

drop table board;












































