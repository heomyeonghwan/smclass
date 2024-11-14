--dual 가상의 테이블,sysdate현재날짜
select sysdate from dual;
select sysdate-30,sysdate,sysdate+30 from dual;

--employees테이블 hire_date 컬럼
select hire_date-1,hire_date,hire_date+1 from employees;

--날짜범위 검색가능, 정렬 order by asc: 순차정렬 desc: 역순정렬
select emp_name,hire_date from employees where hire_date>='02/01/01' and hire_date <='04/12/31'
order by hire_date desc;
select emp_name,hire_date from employees
where hire_date between '02/01/01' and '04/12/31'order by hire_date asc;

--like
select emp_name from employees
where emp_name like '___a%';

select emp_name from employees
where emp_name like '%a___';

--정렬 desc :null 값이 가장 위 acs :null 값이 가장 아래
select department_id from employees
order by department_id desc;

--월급 역순정렬
select emp_name,salary from employees
order by salary desc;

--students 테이블에서 total로 역순정렬
select no,name,total from students
order by total desc;

--hire_date 입사일 기준으로 순차정렬(생략가능)
select * from employees
order by hire_date asc;
-- kor 먼저 정렬후 동일한 값들중에 eng로 정렬
select name,kor,eng,math from students
order by kor desc, eng desc;

--한국어 순차정렬: ㄱㄴㄷ
select name from students
order by name;

--입사일이 빠른 순으로 정렬, 이름은 역순으로 정렬
select hire_date,emp_name from employees
order by hire_date asc,emp_name desc;

-- abs 절대값
select -10 val,abs(-10) as "abs(절대값)" from dual;

select kor,kor-eng,abs(kor-eng) abs from students
order by abs desc;

--floor 소수점 이하버림
select 3.141592, floor(3.141592) from dual;

-- trunc :버림, 자리수 지정
select 34.5678, trunc(34.5678,3) from dual;
select 34.5678, trunc(34.5678,-1) from dual;

--round 반올림, 자리수 범위 지정
select 34.5678, round(34.5678) from dual;
--소수점 둘째자리까지 출력(셋째자리에서 반올림)
select 34.5678, round(34.5678,2) from dual;
-- 양수 첫째자리에서 반올림, 소수점 자리기준 앞쪽으로 한칸위치 반올림
select 34.5678, round(35.5678,-1) from dual;

--ceil 올림 소스점 이하 올림
select 3.141592, ceil(3.141592) from dual;

--mod 나머지
select 27/2, mod(27,2)from dual;
select 30/3, mod(30,3)from dual;
select 30/7, mod(30,7)from dual;

-- 사원번호가 홀수인 사원을 출력
select employee_id,emp_name from employees
where mod(employee_id,2)=1
order by employee_id;

--최종연봉: 월급*12+(월급*12)*커미션, 소수점 2자리에서 반올림해서 첫째자리로 나오게
select salary,round(salary*12+(salary*12)*nvl(commission_pct,0)*1381.86795,1) ysalary from employees;

select round(salary*12+(salary*12)*nvl(commission_pct,0)*1381.86795,1) ysalary from employees;

select * from students;

-- 시퀀스: 자동으로 번호부여
create sequence stu_seq
start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

--시퀀스에서 번호 생성
select stu_seq.nextval from dual;

select stu_seq.currval from dual;

--게시판 테이블생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000), -- varchar2는 4000바이트까지
id varchar2(30),
bhit number(10),
bdate date
);

insert into board values(
1,'제목입니다.','내용입니다.','aaa','1',sysdate
);

insert into board values(
stu_seq.nextval,'제목입니다.2','내용입니다.2','aaa','1',sysdate
);

select * from board;
commit;


create SEQUENCE board_seq
start with 14  --시작번호
increment by 1 --증감숫자
minvalue 1     --최소값
maxvalue 9999  --최대값
nocycle        --cycle : 1~9999이상되면, 다시1
nocache;       --cache : 메모리에 시퀀스값을 미리할당

desc board;
insert into board values(
board_seq.nextval,'제목14','내용14','aaa',1,sysdate
);

select * from board;

update board set btitle='제목을 다시변경' where bno=14;
commit;

drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob,    --대용량 글자타입
id varchar2(20),
bgroup number(4), --답변달기 그룹핑
bstep number(4), -- 답변달기 경우 순서정의
bindent number(4), --답변달기 들여쓰기
bhit number(10),  -- 조회수
bdate date        --등록일

);

select board_seq.currval from dual;

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate
);

select * from board;

--시퀀스 생성
--students_seq.nextval
--students 테이블 100 >101
--101,'홍길순',99,99,90,total,avg,rank,날짜
--1명을 입력하시오

select * from students;

create sequence students_seq

start with 101  --시작번호
increment by 1 --증감숫자
minvalue 1     --최소값
maxvalue 9999  --최대값
nocycle        --cycle : 1~9999이상되면, 다시1
nocache        --cache : 메모리에 시퀀스값을 미리할당
;       

insert into students values(
students_seq.nextval,'홍길순',99,99,90,99+99+90,(99+99+90)/3,0,sysdate
);
select * from students;

delete students where name='홍길순';
commit;
select no,name,kor,eng,math,total,round(avg,2),rank,sdate from students;

select round(avg,2) from students;
--studentㄴ 별칭추가
select s.* ,round(avg,2) from students s;

--10씩증가하는 시퀀스
select dept_seq.nextval from dual;


--s_seq
--시작 1 증분1 최대값 99999
create sequence s_seq
start with 1,
increment by 1,
ninvalue 1,
maxvalue 99999,
nocycle,
nocache
;

--시퀀스 생성, nextval 다음시퀀스번호생성 currval 현재시퀀스번호 보여줌
select s_seq.nextval from dual;
select emp_seq.nextval from dual;


--타입 
--문자형(char,varchar2,nchar,nvarchar2,long,clob),
--char,varchar2 : 한글문자입력시 3byte사용
--varchar2(6): 한글2글자입력
--nvarchar2(5) : 한글 5자리까지 입력가능 - 2byte

--숫자형(number)
--날짜형(date,timestamp)
--timestamp : 밀리세컨드까지 입력(0.001초)
--date : 초까지 입력


select '홍길동' from dual;
--length - 문자길이
select length('홍길동') from dual;
--이름의 길이로 역순 정렬
select name,length(name) n from students order by n desc;
--lengthb - byte크기
select lengthb('홍길동') from dual;


select * from students;

--합계가 200이상이면서 번호가 10에서 50사이면서 이름의 2번째자리에 e가 들어가있는 학생 출력
select * from students
where total>=200 and no>=10 and no<=50 and name like '_e%';

select * from students
where total>=200;

--select * from 테이블(이중쿼리)
select * from(
select * from students
where total>=200
)where name like '_e%' and no>=10 and no<=50;


rollback;

select *from students;

select no,name,total,rank from students;



--등수함수 rank() over(기준점)입력 / no는 중복이 없음,유일키,기본키,프라이머리 키(primary key)
select no, rank() over(order by total desc) ranks from students;

select * from students;

select no,name,total,rank from students
order by total desc;

--수정
update students a
set rank =(
select ranks from(select no, rank() over(order by total desc)ranks from students)b
where a.no=b.no
);

update students a
set rank = 1
where a.no=101;

select * from students order by rank;

rollback;

select no,rank() over(order by total desc) as ranks from students;

update students
set rank = 1
where no = 101;

update students
set rank =2
where no = 96;

update students
set rank =2
where no =64;


--사원번호가 높은순으로 등수를 생성하시오
--등수함수 rank() over(기준점)입력
--사원번호 사원명 등수
select employee_id,emp_name, rank() over(order by employee_id desc) as ranks from employees;

--emp2 테이블 생성 및 employees복사,
create table emp2 as select * from employees;

select rank() over(order by employee_id desc) from employees;

--
desc emp2;
--테이블 rank컬럼추가
alter table emp2 add rank number(4);

desc emp2;

select * from emp2;
--rank()등수를 rank에 입력
update emp2 e set rank = (
select ranks from(select employee_id,rank() over(order byemployee_id desc) ranks from employees)e2
where e.employee_id = e2.employee_id
);

select employee_id,rank from emp2
order by employee_id desc;

select * from emp2;

--컬럼의 순서를 변경
--emp_name 뒤에 rank 컬럼을 배치(숨김)
alter table emp2 modify EMAIL invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify manager_id invisible;
alter table emp2 modify commission_pct invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify retire_date invisible;
alter table emp2 modify department_id invisible;
alter table emp2 modify job_id invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify create_date invisible;
alter table emp2 modify update_date invisible;

--(보이게)
alter table emp2 modify EMAIL visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify hire_date visible;
alter table emp2 modify salary visible;
alter table emp2 modify manager_id visible;
alter table emp2 modify commission_pct visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify retire_date visible;
alter table emp2 modify department_id visible;
alter table emp2 modify job_id visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify create_date visible;
alter table emp2 modify update_date visible;

alter table emp2 modify rank invisible;

alter table emp2 modify rank visible;
select * from emp2;

--컬럼삭제

desc emp2;

alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column salary;
alter table emp2 drop column manager_id;
alter table emp2 drop column commission_pct;
alter table emp2 drop column retire_date;
alter table emp2 drop column create_date;
alter table emp2 drop column update_date;

select * from emp2;

select * from departments;

desc departments;

alter table emp2 add department_name varchar2(80);
--부서명이 없음
select * from emp2;
--부서명은 departments
select * from departments;

select department_id,department_name from emp2;
select department_id,department_name from departments;

update emp2
set department_name ='배송부'
where department_id =50;



----부서명입력
update emp2 e
set e.department_name = 
(
select d from(
select department_id,department_name d from departments)e2
where e.department_id = e2.department_id
);

select department_id,department_name from emp2;

select * from stu;
drop table stu;

--테이블 복사
create table stu as select * from students;

desc stu;

alter table stu drop column rank;
alter table stu drop column total;
alter table stu drop column avg;
select * from stu;

--total 컬럼, avg 컬럼추가하시오
alter table stu add total number(3);
alter table stu add avg number;
alter table stu add rank number(3);

desc stu;

alter table stu modify sdate invisible;
alter table stu modify sdate visible;

select * from stu;
--합계,평균 값추가
update stu set total = kor+eng+math,avg = (kor+eng+math)/3;
--rank 값 추가
select no,total,rank()over(order by total desc) ranks from stu;

update stu set rank =1
where no = 101;

update stu s set rank =
(select ranks from(select no,rank()over(order by total desc) ranks from stu)s2
where s.no = s2.no
);

select * from stu;

commit;

------------날짜함수
--현재날짜:sysdate
select sysdate from dual;
select sysdate-1 from dual;
select sysdate+30 from dual;

create table datetable(
no number(4),
predate date,
today date,
nextdate date
);

--회원가입 1달치,6개월 , 1년
--멤버 파일 결석해서 없음
insert into datetable values(
1,sysdate-30,sysdate,sysdate+180
);
select no,predate,today 가입일,nextdate 완료일 from datetable;

select * from member;
select id,name,mdate,sysdate-mdate from member;
select id,name,mdate,sysdate-mdate from member
where sysdate >=mdate+180;

--입사일 기준 현재날짜가 몇일이 지났는지 출력
--employees, hire_date
select hire_date from employees;
select employee_id,emp_name,sysdate-hire_date from employees;
select employee_id,emp_name,round(sysdate-hire_date) from employees;

-- round 15일 이상이면 1달을 올림 15일 미만이면 일을 초기화
select hire_date,round(hire_date,'month') from employees;

-- trunc 내림 일자를 1로 초기화
select hire_date,trunc(hire_date,'month') from employees;

-- 입사일과 현재일 기준의 달의 수
select hire_date,sysdate,months_between(sysdate,hire_date) from employees;
-- months_between 두 일자 사이의 달의수 알려줌
select hire_date,sysdate,round(months_between(sysdate,hire_date)) 달수,round(sysdate-hire_date) 일수 from employees;

--add_months(,3) 3개월 추가
select select,add_months(hire_date,3)from employees;
--next_day() : 오늘 이후의 수요일 날짜를 알려줌
select sysdate,next_day(sysdate,'수요일')from dual;
select sysdate,next_day(sysdate,'토요일')from dual;

--last_day: 그 달의 마지막 날짜를 알려줌
select hire_date,last_day(hire_date)from employees;
select sysdate,last_day(sysdate)from dual;


---형변환 함수
select sysdate from dual;
select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss')from dual;
-- 날짜 모양 바꾸기
select hire_date from employees;
select hire_date,to_char(hire_date,'yyyy-mm-dd')from employees;

select to_char(to_date('24/01/01'),'yyyy-mm-dd hh24:mi:ss')from dual;

select * from member where id='aaa' and pw='1111';

select * from member;

update member set id='abc', pw='1111', name='허명환',email='gopsl3957@naver.com'
where id='Trineman';

commit;

select * from member where id='eee';



