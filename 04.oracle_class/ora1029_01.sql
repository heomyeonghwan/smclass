-- drop table member;
-- drop table date_tab;
-- drop table no_tab;
--drop table students;

-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제
create table member(
 no number(4),
 id varchar2(20),
 pw varchar2(20),
 name varchar2(20),
 phone varchar2(20),
 mdate date
);

-- insert 데이터 입력 , select 데이터 검색, update 데이터 수정, delete 데이터 삭제
insert into member values(
1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);
insert into member values(
2,'bbb','1111','유관순','010-2222-2222','2024-09-20'
);

-- select 데이터 검색
select * from member;

commit;
rollback;

-- delete 삭제
-- delete member where no=2;
-- delete member;

-- update 수정
update member set name='홍길자' where no=1;
update member set name='김구';
select * from member;

-- create 테이블 생성
create table students (
stuno number(4),
name varchar2(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);

-- sysdate :현재날짜,시간저장
insert into students values(
1,'홍길동',100,100,100+100,sysdate
);

commit;

-- * 모든 컬럼 검색
select * from students;

-- 특정컬럼을 입력하면 컬럼만 검색
select name,sdate from students;

-- 특정컬럼만 입력하면 컬럼입력
insert into students (stuno,name) values(
2,'유관순'
);
select * from students;
--
select * from employees;

-- 테이블을 생성하면서 테이블 내용을 모두 복사
create table emp2 as select * from employees;
select * from emp2;
select count(*) from emp2; --테이블개수

-- 테이블을 생성하면서테이블 구조만 복사
create table emp3 as select * from employees where 1=2;
select * from emp3;

-- 테이블이 존재 할 경우 데이터만 복사
create table member2 as select * from member where 1=2;
insert into member2 select * from member;

--테이블컬럼
--컬럼데이터 타입 길이 변경
--alter변경 member테이블 no컬럼의 타입길이를 변경
alter table member modify no number(10);
--alter변경, 컬럼의 이름을 변경
alter table member rename column no to memberNo;


--테이블 구조
desc employees;
-- employees 테이블에서 사원번호(employee_id),사원이름(emp_name),입사일 (hire_date)
select employee_id,emp_name,hire_date
from employees;

SELECT * FROM employees;

-- 연산자 : 산술 연산자, +,-,*,/

--drop table member;
--drop table member2;
--drop table emp2;


select kor,eng,(kor+eng) from students;
select kor,eng,(kor+eng),abs(kor-eng) from students;

select * from employees;

--문자 더하기 안됨
select employee_id,emp_name from employees;

--concat 명령어, ||
select concat(employee_id,emp_name) from employees;
select employee_id||emp_name from employees;

--달러 환산 1384
select salary from employees;
select salary*1384 from employees;

--문자로 변환, 천단위 표시
select to_char(salary*1384,'999,999,999')from employees;
select emp_name,salary,salary*1384 from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

insert into stu values(1,'홍길동',100);
insert into stu values(1,'유관순',99);

commit;

insert into stu values(3,'',0);
insert into stu values(4,null,null);


--null 값을 검색 is null
select *from stu where name is null;

-- null이 아닌것을 출력 : is not null
select commission_pct from employees where commisstion_pct is not null;

select salary from employees;
--연봉계산 *12
select salary, salary*12 from employees;
select salary, salary*12, salary*12*1384 from employees;

--커미션이 없는 사원은 null값이 있는데, null + ,-, *, /  null 값으로 변경
select salary, salary*12, salary*12+(salary*12)*commission_pct*0.01 from employees;
--컬럼명 별칭사용 as, ""특수문자,사이공간까지 컬럼명으로 사용가능
select salary, salary*12 as 년봉, salary*12+(salary*12)*nvl(commission_pct,0)*0.01 as "R e a l_yearsalary" from employees;

--nvl() 함수 nvl(kor,0):kor 컬럼에 null 값이 있으면 0으로 표시
select * from stu;
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu;

--번호 이름,국어,영어 수학,합계,평균,등수, 입력일 컬럼명 별칭을 사용해서 출력
select * from students;
select no as 번호,name as 이름,kor as 국어,eng "영 어",math 수학,total 합계,avg 평균,sdate 입력일
from students;
--사원번호,이름,이메일을 합쳐서 출력
select employee_id||emp_name||email from employees;
select concat(concat(employee_id,emp_name),email) from employees;
select emp_name||' is a '||job_id from employees;

--중복제거 : distinct
select department_id from employees;
select distinct department_id from employees;

--정렬 : order by - asc 순차정렬:생략가능 desc 역순정렬
select distinct department_id from employees order by department_id desc;

--job_id 중복제거 출력
select distinct job_id from employees;
select job_id from employees; --원래거

--문자열 자르기 substr(0,2) 0,1 출력
select substr(job_id,0,2) from employees;
---4번째부터 컬럼데이터를 가져와서 중복을 제거
select distinct substr(job_id,4) from employees;

--where 절 : 조건비교연산자 >,<,>=,<=,=,!=
select * from employees;

select * from employees where manager_id != 124;
select * from employees where job_id = 'SH_CLERK';

select * from employees where employee_id > 100;

--students 합계 250점 이상 출력
select * from students where total >=250;

--합계 250이상이면서kor 90점 이상  출력
select * from students where total >= 250 and kor >=90;

--영어 점수 70이상 90 이하 출력
select * from students where eng >=70 and eng <=90;

--월급이 5000이상 8000이하
select * from employees where salary>= 5000 and salary <=8000;

--월급이 7000이 아닌것을 모두 출력 !=, ^=, <>
select * from employees where salary != 7000;

-- department_id 50인것과 50이 아닌것의 갯수
--count 갯수
select * from employees where department_id = 50;
select count(*) from employees where department_id = 50;
select count(*) from employees where department_id != 50;

select count(*) from employees where department_id is null;

--null 값은 count()에 포함안됨
select count(department_id) from employees;
select count(*) from employees;

-- 급여 4000이하 사원번호 사원명 급여 컬럼만 출력
select employee_id 사원번호,emp_name 사원명,salary 급여 from employees where salary <= 4000;

-- 숫자인경우 비교연산자 가능, 날짜 비교연산자 가능
select emp_name,hire_date from employees;
select * from employees where hire_date >= '2002/01/01';

--1999/12/31 이전에 입사한사람을 출력
select emp_name,hire_date from employees where hire_date <= '1999/12/31';

--2001/01/01 부터 2004/12/31까지 출력
select emp_name,hire_date from employees
where hire_date >= '2001-01-01' and hire_date <= '20041231';


-- 논리 연산자
--국어 점수가 90이상 또는 영어점수가 90이상을 출력
select * from students where kor >= 90 or eng >=90;
select count(*) from students where kor >= 90 and eng >=90;
select count(*) from students where not kor >=90;

-- 부서번호 department_id = 80,이면서 job - man 인경우
select * from employees
where department_id =80 or substr(job_id,4) = 'MAN';
select * from employees where department_id =80 or job_id = 'SA_MAN';

-- 커미션 0.2,0.3,0.5 인경우만 출력
select commission_pct from employees where commission_pct is not null;
--출력1
select commission_pct from employees where commission_pct =0.2 or commission_pct =0.3 or commission_pct = 0.5;
--출력2 in 연산자
select commission_pct from employees where commission_pct in (0.2,0.3,0.5);

-- 사원번호가 110번,120,130
select employee_id from employees where employee_id = 110 or employee_id = 120 or employee_id =130;
select * from employees where employee_id in (110,120,130);

-- 150 ~ 170사원번호 출력
--between  : <= 포함이 되어있는 경우만 해당 (날짜도 가능)
select * from employees where employee_id >150 and employee_id < 170;
select * from employees where employee_id between 150 and 170;

-- 날짜 between
select hire_date from employees where hire_date in ('2004/02/17','2002/06/07');
select hire_date from employees where hire_date between '2002/06/07' and '2004/02/17';

-- job Man 출력
--like 연산자 : 포함되어있는 글자검색
select * from employees where substr(job_id,4)='MAN';
select * from employees where job_id like '%MAN';
select * from employees where job_id like 'ST%';

--emp_name  소문자 a가 들어가있는 이름을 출력
select * from employees where emp_name like '%a%';
select * from employees where emp_name not like '%a%';

-- 2번쨰 자리에 t가 들어가있는 이름출력
select * from employees where emp_name like '_t%';
select * from employees where emp_name like '___v%';
--뒤에서 두번째자리 n
select * from employees where emp_name like '%l_';

--첫번째 D가 들어가있는 이름
select * from employees where emp_name like 'D%';








