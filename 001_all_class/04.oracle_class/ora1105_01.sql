--join
--inner join(equi join,non-equi join),self join,outer join

--equi join
-- employees 에서 사원번호 사원명 부서번호 부서명 출력
select employee_id,emp_name,a.department_id,department_name
from employees a,departments b
where a.department_id=b.department_id;

--non-equi join
-- 두테이블 간 동일한 컬럼없이 데이터를 가져오는 방법
-- avg 값을 가지고 다른 컬럼을 다른테이블에 가져와 출력
select * from stu_grade;
select * from students;

select name,avg,grade from students,stu_grade
where avg between loavg and hiavg;

--self join
-- 자신의 테이블을 2번호출
select a.employee_id,a.emp_name,a.manager_id,b.emp_name 
from employees a,employees b
where a.manager_id=b.employee_id;

select * from stu;
--컬럼삭제
alter table stu drop column result;
--컬럼 추가
alter table stu add result varchar2(10);
--avg의 컬럼을 사용해 stu_grade 활용한 값을 result컬럼에 모두 입력
--no,avg,result 출력
select no,avg,result from stu;

select no,avg,result,grade 
from stu,stu_grade
where avg between loavg and hiavg;
--1.non-equi join update구문
update stu set result =(
select grade
from stu_grade
where avg between loavg and hiavg
);
--2.non-equi join update구문
update stu a set result=(
select results from(
select no,grade as results
from stu,stu_grade
where avg between loavg and hiavg
)b
where a.no = b.no
);

--rank() over() 등수함수
update stu set rank=0;

select no,rank() over(order by avg desc) as ranks from stu;

--ranks() 의 결과값으 rank 결럼에  모두압력하시오
--1번 방법은안됨

update stu a set rank=(
select ranks from(
select no,rank() over(order by avg desc) as ranks from stu
)b
where a.no = b.no
)
;

--outer join
--107개 :null 값 포함 갯수
select employee_id,emp_name,manager_id from employees;

--106개 :null 값 제외 갯수
select count(manager_id) from employees
where manager_id is not null;

--null 값일때 0 출력 ceo
select nvl(manager_id,0) from employees;
select nvl(to_char(manager_id),'CEO') manager_id from employees;

--self join manager_id 매니저의 이름을 출력
--self join 106개
--outer join : 해당컬럼에 null값이 존재할시 null값 포함해서 출력
select a.employee_id,a.emp_name,a.manager_id,b.emp_name 
from employees a,employees b
where a.manager_id=b.employee_id(+); --outer join

-- 사원번호 사원명 부서번호 부서명
select employee_id,emp_name,a.department_id,department_name 
from employees a,departments b
where a.department_id=b.department_id;

--부서번호 null 값도 출력
select employee_id,emp_name,a.department_id,department_name 
from employees a,departments b
where a.department_id=b.department_id(+);


--ansi cross join
select * from employees cross join departments;
-- cross join
select * from employees,departments;

--ansi inner join
select a.department_id,department_name
from employees a inner join departments b
on a.department_id=b.department_id;
--ansi inner join: using : 공통적인게 있을때
select department_id,department_name
from employees inner join departments
using (department_id);
-- equi join
select a.department_id,department_name
from employees a,departments b
where a.department_id=b.department_id;

--ansi join : natural join : 두개의 공통부분 컬럼이 있으면 자동으로 인식해서 검색
select department_id,department_name
from employees natural join departments;

-- ansi outer join(left,right,full)
select employee_id,emp_name,a.department_id,department_name
from employees a left outer join departments b
on a.department_id=b.department_id;

--오라클 outer joim 두개컬럼의 (+)는 에러
select a.employee_id,a.emp_name,a.manager_id,b.emp_name 
from employees a,employees b
where a.manager_id=b.employee_id(+);


--union
select * from students;

select * from students
where total>=250; --24개

select * from students
where name like '%a%';--35개

--union 중복은 제외 49개
--union all : 중복 허용
select * from students
where total>=250
union
select * from students
where name like '%a%';

select * from students
where total>=250 or name like '%a%';

--union : 같은테이블 다른테이블 모두 사용이 가능, 컬럼의 타입만 맞으면 모두 출력
--조건  위쪽 쿼리문과 아래 쿼리문 개수 및 타입이 동일해야함
--자유게시판 공지사항 이벤트 종합게시판 등을 통합적으로 검색해서 출력하고싶을때 사용
select employee_id,emp_name from employees;
select no,name from students;

select employee_id,emp_name from employees
union
select no,name from students;


-- employees에 없는 departments의 부서검색 >부서번호 부서이름
select department_id,department_name
from departments a
where not exists
(select 1 from employees b where a.department_id=b.department_id);
--1은 의미없음
-- employees department_id 가 50인 사원 > 부서번호 부서이름
select a.department_id,department_name from employees a,departments b
where a.department_id=b.department_id and a.department_id =50;
-- employees 에 salarㅛy 5000 and 8000 사원ㅇ의 부서번호 부서이름
select a.department_id,department_name 
from employees a,departments b
where a.department_id=b.department_id
and salary >=5000 and salary <=8000;

--두개를 유니온
select a.department_id,department_name from employees a,departments b
where a.department_id=b.department_id and a.department_id =50
union
select a.department_id,department_name 
from employees a,departments b
where a.department_id=b.department_id
and salary >=5000 and salary <=8000;

--두개를 유니온
select a.department_id,department_name from employees a,departments b
where a.department_id=b.department_id and a.department_id =50
union
select department_id,department_name
from departments a
where not exists
(select 1 from employees b where a.department_id=b.department_id);

--
select name,mdate from member
union
select name,sdate from students;


--
select * from board;

drop table board2;

create table board2 (
	bno number(4),
	btitle VARCHAR2(1000),
	bcontent clob,
	id VARCHAR2(30),
	bgroup number(4),
	bstep number(4),
	bindent number(4),
	bhit number(4),
	bdate DATE,
	bfile VARCHAR2(100)
);



select * from board2;

commit;

delete board2 where bno=98;

select * from board2
where bno between 1 and 20
;
--rownum : 번호를 새롭게 부여
select rownum,bno,btitle,bdate from board2
order by bdate desc,btitle asc;

--rownum 번호가 순서대로 정렬됨, 서브쿼리  사용
select rownum,bno,btitle from(
select bno,btitle from board2 order by bdate desc)
;

select rnum,bno,btitle from
(select rownum rnum,bno,btitle from(
select bno,btitle from board2 order by bdate desc))
where rnum between 11 and 20;

--row_number() over() : 정렬한 후 번호를 부여
select row_number() over(order by bdate desc) rnum,bno,btitle,bdate from board2;

select rnum,bno,btitle,bdate from(
select row_number() over(order by bdate desc) rnum,bno,btitle,bdate
from board2)
where rnum between 11 and 20
;

select * from(
select row_number() over(order by bdate desc) rnum,a.* from board2 a)
where rnum between 11 and 20
;

select bno,a.* from board2 a;

-- 모든컬럼을 출력하시오 rownum 사용
-- 11~20 
select * from
(select rownum rnum,a.* from(
select * from board2 order by bdate desc)a)
where rnum between 11 and 20;

--rownum
select rownum,rank() over(order by avg desc) from students;

select * from
(select rownum rnum,a.* from(
select no,name,rownum,rank() over(order by avg desc) from students
)a)
where rnum between 11 and 20
;



--row_number() over()

select * from(
select row_number() over(order by avg desc) rnum,rank() over(order by avg desc),
a.* from students a)
where rnum between 21 and 30;

--rank() 함수
select no,name,avg,rank() over(order by avg desc) from students;

--rank() 값 rank컬럼에 입력
update students set rank =1
where no=1;

update students a set rank =(
select ranks from(
select no,rank() over(order by avg desc) ranks from students 
)b
where a.no=b.no);

commit;
select *from students;


--view

select * from employees;

create or replace view employees_view
as select employee_id,emp_name,email,phone_number,hire_date
from employees;

--employees_view
select * from employees_view;
--사원번호 사원명 이메일 폰번호 입사일 부서번호 부서명 출력

select employee_id,emp_name,email,phone_number,hire_date,a.department_id,department_name
from employees a,departments b
where a.department_id=b.department_id;
--view 생성
create or replace view emp_view
as
select employee_id,emp_name,email,phone_number,hire_date,a.department_id,department_name
from employees a,departments b
where a.department_id=b.department_id;

select * from emp_view;
--view 삭제
drop view emp_view;

--view 컬럼 커멘트(주석-설명문)추가
comment on column employees_view.employee_id is '사원번호에 해당됩니다.';
--컬럼 커멘트 주석 확인
select * from user_col_comments;
--테이블 커멘트 주석확인
select * from user_tab_comments;

--
select * from emp02;

drop table emp02;

create table emp02(
employee_id number(6),
emp_name varchar2(80),
hire_date date,
salary number(8,2),
department_id number(6)
);

desc emp02;

insert into emp02(employee_id,emp_name,hire_date,salary,department_id)
select employee_id,emp_name,hire_date,salary,department_id
from employees;

select * from emp02;
--view 생성
-- with read only select만 가능 insert delete update 불가
create or replace view emp02_view
as
select employee_id,emp_name,hire_date
from emp02
with read only;

drop view emp02_view;

--view select
select * from emp02_view order by employee_id;

--단순 view:  1개의 테이블로 구성된 것
--insert update delete 가능, not null 등 제약조건이 있으면 insert 불가할수있음
--복합 view :  2개이상 테이블조인,함수사용,group by 같은경우
--insert update delete 불가
-- 100번 이름을 홍길동
update emp02_view set emp_name='홍길동'
where employee_id=101;

insert into emp02_view values(
207,'유관순',sysdate
);
delete emp02 where employee_id = 207;
select * from emp02_view order by employee_id desc;

select * from emp02;

alter table emp02 modify salary number(8,2) not null;









select * from students;
--no : seq
--입력데이터: name,kor,eng,math
--total: 오라클에서 계산
--avg: 오라클에서 계산
--rank: 오라클에서 계산
--sdate: sysdate오라클에서 계산

insert into students values(students_seq.nextval,name,kor,eng,math,
kor+eng+math,(kor+eng+math)/3,sysdate);

-- students 테이블에 no가 가장큰수
select max(no) from students;

select * from students;


--avg 소수점 2자리까지만 출력하시오
-- no name kor eng math total avg rank sdate
select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students
;

-- a가 포함되어있는 이름을 검색
select * from students where name like '%a%'
;

select * from students order by name desc
;














