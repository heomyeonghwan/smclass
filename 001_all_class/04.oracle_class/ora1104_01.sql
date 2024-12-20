drop table emp02;

drop table mem2;

select * from mem;

create table emp02(
empno number(4) not null,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
1,'홍길동','clerk',2
);

insert into emp02 values(
2,'유관순',null,null
);
--not null
insert into emp02 values(
null,'이순신',null,null
);

drop table emp02;

create table emp02(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
1,'홍길동','clerk',2
);

insert into emp02 values(
2,'유관순',null,null
);

insert into emp02 values(
3,'이순신',null,null
);

insert into emp02 values(
null,'강감찬',null,null
);
--unique 중복안됨
insert into emp02 values(
2,'김구',null,null
);

select * from emp02;

delete emp02 where empno is null;
commit;
-- 제약조건변경 alter
alter table emp02 modify empno not null;
alter table emp02 modify empno;

-- not null, pk_emp02_empno별칭
alter table emp02 add constraint pk_emp02_empno primary key(empno);

alter table emp02 drop constraint pk_emp02_empno;

create table emp02(
empno number(4) primary key,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

drop table mem;
create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(100) default '무명',
gender varchar2(6) check(gender in ('Male','Female'))
);

insert into mem values(
'aaa','1111','홍길동','Male'
);
insert into mem values(
'bbb','1111','유관순','Female'
);
commit;

create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
id varchar2(30),
constraint fk_board2_id foreign key(id) references mem(id)
);

select * from mem;
-- 외래키로 등록시 부모키에 해당값이 없을시 에러
insert into board2 values(
3,'제목3','ccc'
);

--외래키삭제
alter table board2 drop constraint fk_board2_id;


--부모키 삭제시 외래키로 등록된 값들을 모두 삭제
alter table board2
add constraint fk_board2_id foreign key(id)
references mem(id) on delete cascade;--on delete set null

--default : on delete restricted : 부모키 삭제시 외래키에 등록된 값이 있으면 삭제가 되지않음
--on delete set null: 부모키 삭제시 외래키로 등록된 값을 삭제하지않고  해당되는 컬럼값만 null 처리

--부모테이블의 aaa삭제시 자식테이블의 aaa글이 모두 삭제
delete mem where id='aaa';

commit;
select * from board2;

drop table mem;
drop table board2;

create table mem(
id varchar2(30) primary key,
pw VARCHAR2(100) not null,
name varchar2(100),
deptno number(4)
);
insert into mem values(
'aaa','1111','홍길동',10
);
insert into mem values(
'bbb','1111','유관순',20
);

insert into mem values(
'ccc','1111','이순신',30
);
commit;
select * from mem;

-- 10 '총무부', 20 '인사부', 30 '마케팅'

------------decode if문과 비슷
select id,pw,name,deptno,
decode(deptno,
10,'총무부',
20,'인사부',
30,'마케팅'
)
from mem;

select * from employees;

select job_id from employees;

--clerk: 5%,rep- 10%, man: 15% 급여인상
--1.clerk,rep,man 을출력
select job_id from employees;
--1번째에서 3개를 가져오기
select substr(job_id,1,3) from employees;
select substr(job_id,4) j_id from employees
where lower(substr(job_id,4)) in('clerk','rep','man');-- 소문자로 검색 lower

select substr(job_id,4) j_id,salary,
decode(substr(job_id,4),
'CLERK',salary*1.05,
'REP',salary*1.1,
'MAN',salary*1.15
) sal
from employees
where substr(job_id,4) in('CLERK','REP','MAN');


select * from lavel_data;

--1:100포인트 2:1000포인트 3:5000포인트 4:10000포인트 5:20000포인트
--decode 일치하는 경우에만 사용가능
select id,lavel,
decode(lavel,
1,100,
2,1000,
3,5000,
4,10000,
5,20000
)||' point' as point
from lavel_data;

--1,2,3:5000포인트4,5:20000vhdlsxm
select id,lavel,
case
when lavel>=1 and lavel <=3 then 5000
when lavel>=4 and lavel <=5 then 20000
end point
from lavel_data;

--decode: 일치하는 경우에만 사용가능
--case : decode 와 같지만 비교연산자를 사용할수 있음
select id,pw,name,deptno,
case
when deptno=10 then '총무부'
when deptno=20 then '인사부'
when deptno=30 then '마케팅'
end as deptName
from mem;

--avg 90이상 A 80이상 B 70: c 60:d, f
--result 컬럼을 출력

select * from students;

select name,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
when avg<60 then 'F'
end as result
from students;

--테이블 전체복사
create table stu as select * from students;

--컬럼추가
select * from stu;
alter table stu add result varchar2(2);

--result 컬럼에 추가
select
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
when avg<60 then 'F'
end as result
from stu;

update stu set result =(
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
when avg<60 then 'F'
end 
);
select * from stu;

--파이썬에서 if문 구현해서 처리
--rank() over() 순위를 구현하는 함수/중복순의 갯수만큼 다음순위값 증가 표시
select no,name total, rank() over(order by total desc)from stu
order by no;
--dense_rank: 중복순위가 존재해도 순차적으로 다음순위 표시
select no,name total, dense_rank() over(order by total desc)from stu;

--순위를 rank  컬럼에 추가
select ranks a from
(select rank() over(order by total desc) ranks from stu b);
--랭크 등수 입력처리
update stu a set rank= 
(
select ranks a from(
select no,rank() over(order by total desc) as ranks from stu)b
where a.no = b.no
);

select no,rank from stu;
select no,rank() over(order by total desc) as ranks from stu;

--case
--salary 5000 이하 월급의 15%인상 5000~8000 10%인상 8000이상 5%인상 해서 출력

select salary,
case
when salary <= 5000 then salary*1.15
when salary >= 5000 and salary <=8000 then salary*1.1
when salary > 8000 then salary*1.05 
end y_salary
from employees;

-- emp_name 대문자 D가 포함되어있으면 10%인상, M이 5% 그외는 0%인상
select emp_name,salary,
case
when emp_name like '%D%' then salary*1.1
when emp_name like '%M%' then salary*1.05
else salary
end y_salary
from employees;

select * from employees;

select department_id,commission_pct from employees
where commission_pct is not null;

--커미션이 있는 사원수를 출력
select count(emp_name) from employees
where commission_pct is not null;

--부서별 사원수를 출력
select department_id,count(*) from employees
group by department_id
order by department_id;

--부서별 평균월급을 출력
select department_id,avg(salary) from employees
group by department_id;

--그룹함수 조건을 사용하려면 having절을 사용함
--부서별 평균월급이 7000보다 높은 사람의 인원수를 출력
select department_id,avg(salary),count(salary) from employees
group by department_id
having avg(salary)>=7000;

-- 전체 평균월급보다 적게 받는 부서별 사원수를 출력하시오.
select avg(salary) from employees;

select department_id,avg(salary),count(salary) from employees
where salary<(select avg(salary) from employees)
group by department_id
;
--부서별 평균월급이 6000이하인 부서별 인원수를출력하시오
--그룹함수는 having절에 조건문을 사용함,where절 불가
select department_id,avg(salary),count(salary) from employees
group by department_id
having avg(salary) <6000;
--부서번호와 부서별 평균월급
select department_id,avg(salary) from employees
group by department_id;
--부서번호,개인별월급 인우ㅡㅓㄴ
select department_id,salary,count(*) from employees
group by department_id,salary;

--부서별 평균월급보다 적게받는 사원을 출력
select department_id,emp_name,salary from employees a
where salary<
(
select salarys from(
select department_id,avg(salary) salarys from employees
group by department_id)b
where a.department_id = b.department_id
)
;
--부서별 평균월급보다 적게받는 사원수을 출력
select department_id,count(*) from employees a
where salary<
(
select salarys from(
select department_id,avg(salary) salarys from employees
group by department_id)b
where a.department_id = b.department_id
)
group by department_id
;

-- 부서의 최대급여와 최소급여를 출력, 최대급여가 5000이상인 부서만 출력
select department_id, max(salary),min(salary) from employees
group by department_id
having max(salary)>5000
order by department_id desc;

-- 학번 이름 전화번호 주소 성별 학년 학기 국어 영어 수학 합계 등수
-- 1001 홍길동 010 서울 남자 1 1 100 100 100 300 1
-- 1001 홍길동 010 서울 남자 1 2 90 90 90 270 8
-- 1001 홍길동 010 서울 남자 1 3 95 95 95 285 15
-- 1001 홍길동 010 서울 남자 1 4 100 100 99 299 2
-- 1001 홍길동 010 서울 남자 2 1 100 100 100 300 1
-- 1001 홍길동 010 서울 남자 2 2 90 90 90 270 8
-- 1001 홍길동 010 서울 남자 2 3 95 95 95 285 15
-- 1001 홍길동 010 서울 남자 2 4 100 100 99 299 2
-- 1001 홍길동 010 서울 남자 3 1 100 100 100 300 1
-- 1001 홍길동 010 서울 남자 3 2 90 90 90 270 8
-- 1001 홍길동 010 서울 남자 3 3 95 95 95 285 15
-- 1001 홍길동 010 서울 남자 3 4 100 100 99 299 2


-- 부서명 departments
select * from departments;

select * from employees;

--Donald OConnell 의 부서명

select emp_name,department_id from employees
where emp_name='Donald OConnell';

select department_id,department_name from departments
where department_id=50;

--join을 사용해야 두개의 쿼리를 1개위 쿼리로 구성이 가능해짐
--join
--1. cross join : 특별한 키워드없이 두개의 테이블을 검색하는 것
--2. inner join (equi join, non-equi join)
--3. outer join
--4. self join

--1. cross join : 특별한 키워드없이 두개의 테이블을 검색하는 것
select * from employees; --107
select * from departments; --27

select count(*) from employees,departments; --2889
select * from employees,departments;

-- inner join: equi join 같은 컬럼을 가지고 비교해서 두개의 테이블을 검색
select emp_name,a.department_id,department_name
from employees a,departments b
where a.department_id = b.department_id(+);


select * from member;
select * from board;

select bno,btitle,bcontent,a.id,email,phone 
from member a,board b
where a.id=b.id
;


--inner join: 사원번호 사원명 잡아이디 잡타이틀을 출력하시오
select * from jobs;

select employee_id,emp_name,a.job_id,job_title
from employees a,jobs b
where a.job_id=b.job_id and a.job_id='SH_CLERK';

--사원번호 사원명 부서번호 부서명 잡아이디 잡타이틀을 출력
select employee_id,emp_name,a.department_id,department_name,a.job_id,job_title
from employees a,departments b,jobs c
where a.job_id=c.job_id and a.department_id=b.department_id;

--member 이름
--board 게시글
select bno,btitle,bcontent,name,bgroup,bstep,bindent,bhit,bdate,bfile
from member a,board b
where a.id=b.id;

--사원번호 사원명 월급 부서번호 부서명
--월급 평균 월급보다 적은 사원을 출력
select employee_id,emp_name,salary,a.department_id,department_name
from employees a,departments b
where a.department_id=b.department_id
and salary <(select avg(salary) from employees)
;

--q부서별 평균월급보다 작은 사원을 출력

--1.부서별 평균월급
select department_id,avg(salary) from employees
group by department_id;
--
select employee_id,emp_name,salary,a.department_id,department_name
from employees a,departments b
where a.department_id=b.department_id
and salary < 
(select salarys from
(select department_id,avg(salary) salarys from employees
group by department_id)c
where a.department_id=c.department_id)
;

--
select * from employees;
-- job_id가 CLERK 인 사원의 사원명 사원번호 부서명 부서번호 잡아이디 잡타이틀 출력

select emp_name,employee_id,a.department_id,department_name,a.job_id,job_title
from employees a,departments b,jobs c
where a.department_id=b.department_id and a.job_id=c.job_id and substr(a.job_id,4) in ('CLERK','MAN');

select salary from employees
order by salary;
-- 2000~4000E등급 4000~6000D 6000~8000C 8000~10000B 10000~100000A

create table salgrade(
grade varchar2(10),
losal number(6),
hisal number(6)
);

insert into salgrade values(
'E등급',2000,4000
);
insert into salgrade values(
'D등급',4001,6000
);
insert into salgrade values(
'C등급',6001,8000
);
insert into salgrade values(
'B등급',8001,10000
);
insert into salgrade values(
'A등급',10001,100000
);

select * from salgrade;

commit;

drop table stu_grade;

--salary 옆에 등급 넣기
--등급은 salgrade 있음 employees와 같은컬럽없음
-- non-equi join을 사용해서 테이블 join하려함

-- non-equi join: 두테이블 같은 컬럼없으면서 두테이블값을 비교해서 출력
select emp_name,salary,grade 
from employees,salgrade
where salary between losal and hisal;

-- non-equi join 활용하여 students ABCDF 등급을 출력하시오
--100 ~90 89~80... stu_grade

create table stu_grade(
grade varchar2(10),
loavg number(6),
hiavg number(6)
);
insert into stu_grade values(
'F등급',0,59
);
insert into stu_grade values(
'D등급',60,69
);
insert into stu_grade values(
'C등급',70,79
);
insert into stu_grade values(
'B등급',80,89
);
insert into stu_grade values(
'A등급',90,100
);

select * from stu_grade;
commit;
select name,avg,grade 
from students,stu_grade
where avg between loavg and hiavg;

-- non-equi join 활용하여 이룍
update stu set result='';
commit;
select * from stu;



desc stu;

alter table stu modify result varchar2(10);

create table stu_grade(
grade varchar2(10),
loavg number(5,2), --5자리중에 2자리 소수점
hiavg number(5,2)
);
insert into stu_grade values(
'F등급',0,59.99
);
insert into stu_grade values(
'D등급',60,69.99
);
insert into stu_grade values(
'C등급',70,79.99
);
insert into stu_grade values(
'B등급',80,89.99
);
insert into stu_grade values(
'A등급',90,100
);

select * from stu_grade;
commit;

select name,total,avg,grade
from stu,stu_grade
where avg between loavg and hiavg;

update stu a set result=(
select results from(
select no,grade as results
from stu,stu_grade
where avg between loavg and hiavg
)b
where a.no = b.no
);

select * from stu;


-- self join : 자신의 테이블 2개를 join 하여 결과값을 출력
select employee_id,emp_name,manager_id from employees;

select employee_id,emp_name,manager_id from employees
where employee_id=124;

select a.employee_id,a.emp_name,a.manager_id,b.emp_name
from employees a,employees b
where a.manager_id=b.employee_id and a.manager_id=124;



--------------------------
select * from students;

desc students;

select * from students;

select students_seq.currval from dual;








