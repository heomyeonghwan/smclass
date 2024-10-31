select * from member;

update member set id='abc',pw='1111',name='허명환',email='gopsl3057@naver.com'
where id='abc';

commit;

select * from member;

update member set pw='1111' where id='Towell';
---------------------------------------------------
--------날짜 함수
select sysdate-1,sysdate,sysdate+1 from dual;
-- round 반올림
select hire_date,round(hire_date,'month') from employees;
-- trunc 내림
select hire_date,trunc(hire_date,'month') from employees;

select trunc(sysdate,'month') from dual;
-- add_months 다음달(달수를 더함)
select add_months(trunc(sysdate,'month'),1) from dual;

--vip요금제로 변경을하면 다음달 1일부터 혜택
select sysdate,add_months(trunc(sysdate,'month'),1) from dual;

--입사일 기준 다음달 1일부터 혜택을 줌, 입사일 다음달 1일 출력
select hire_date,add_months(trunc(hire_date,'month'),1) as 다음달 from employees;

--입사일 기준 1년 후 날짜를 출력
select hire_date,add_months(hire_date,12) from employees;
select hire_date,hire_date+365 from employees;

--입사일 기준 달의 마지막 날짜
select hire_date,last_day(hire_date) from employees;

--입사일기준 1년후 날짜와 1년후 마지막 그달의 날짜를 출력
select hire_date,add_months(hire_date,12),last_day(hire_date+365) from employees;

--입력일 기준 1년 후 마지막 날짜가 24,25년 8월31일 9월 30일 또는 10월31일인 학생들을 모두출력
select sdate from students;

select name,sdate,last_day(sdate+365) sdate2 from students 
where last_day(sdate+365) in('24/08/31','24/11/30','24/12/31','25/08/31','25/09/30','25/10/31')
order by sdate2;

select sdate,extract(month from sdate),extract(month from last_day(sdate+365)) from students
where extract(month from last_day(sdate+365)) in (8,11,12);

--extract 함수 : 특정 년 월 일 시 분 초 분리해서 가져오는 함수
--년원일 분리(sysdate)/systimestamp 다분리
select sysdate from dual;
select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

--substr함수 :  문자에서 시작위치 가져올개수
select sysdate,substr(sysdate,4,2) from dual;

select sdate,last_day(sdate+365) sdate2 from students
where substr(last_day(sdate+365),4,2) in (6,8,12)
order by sdate2;


---- to_char 날짜 형변환해서 날짜 포멧을 변경
--date타입에서 > char타입으로 변경해서 포멧

--날짜 > 문자 : to_char  ##날짜포맷
--문자 > 날짜 : to_date  ##날짜 사칙연산
--숫자 > 문자 : to_char  ##천단위, 숫자앞에 0을 표시, 통화 표시
--문자 > 숫자 : to_number ## 천단위 표시, 천단위 삭제해서 사칙연산
select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd')from dual;
select sysdate,to_char(sysdate,'yy-mm-dd')from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss day')from dual; --24시 표현
select sysdate,to_char(sysdate,'yy-mm-dd am hh:mi:ss dy')from dual;--am 오전 오후
select sysdate,to_char(sysdate,'yy-mon-dd hh:mi:ss')from dual;

select hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss') from employees;

--students 테이블 sdate를 2024/01/01 형태로 출력
select sdate,to_char(sdate,'yyyy/mm/dd') from students;
--
select kor from students
where kor = 70;

--숫자 > 문자 변경해서 포멧 천단위 표시
select salary*1382.86*12 from employees;
--자리수 채우기 9는 빈공백 0은 0으로 채움
--L :국가 통화기호 표시, $: $표시가 됨
select to_char(salary*1382.86*12,'L00,999,999,999.99') from employees;

select to_char(1,'000') from dual;
select 12 from dual;

select to_char(123456,'000000000'),
to_char(123456,'999,999,999') from dual;

--
create table  chartable(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);

create table  chartable2(
no number(4),
kor number(10),
kor_char number(10),
kor_mark number(10)
);

--숫자형 타입은 숫자앞에 0이 있어도 표시가 안됨 : 문자형타입만 가능
--천단위 표시는 숫자형타입에 입력이 안됨 : 문자형타입에만 가능
insert into chartable2 values(
3,3000000,3000000,3000000
);

select * from chartable2;

-- number,number, str-number타입을 넣어도 입력
--문자형 타입에는 숫자형타입 가능
insert into chartable values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);

select * from chartable;

--숫자형타입 문자형(숫자)타입은 사칙연산가능
--숫자형타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능, 천단위표시는 문자형타입
select kor*kor_char from chartable;
select kor+kor_mark from chartable;

desc chartable;
desc chartable2;--모든타입넘버


--2일이후의 날짜를 출력
-- to_date 날짜형으로 변환
select '20241031' from dual;
select '20241031',to_date('20241031')+2 from dual;

select sysdate,sysdate+2 from dual;

select to_date(20241031) from dual;
--number 형 > 날짜형타입
select sysdate - to_date(20231101) from dual;
--문자형 > 날짜형타입
select sysdate - to_date('20231101') from dual;

--문자형 > 숫자형 타입
select '20,000' from dual;
--천단위 문자형타입 > 천단위 제외 숫자형 타입
select to_number('20,000','999,999') from dual;

select * from chartable;
--문자형 천단위 타입 > 숫자형타입변환
select kor,to_number(kor_mark,'999,999,999')from chartable;
--숫자형타입이라 사칙연산가능
select kor+to_number(kor_mark,'999,999,999')from chartable;

--
select department_id from employees;
-- department_id 에 null찾기
select department_id from employees
where department_id is null;
-- commission_pct 에 null찾기
select commission_pct from employees
where commission_pct is null;


--월급*커미션 계산하기
select salary+salary*nvl(commission_pct,0) from employees;

--null인경우 0표시
--null인경우 CEO표시
select department_id from employees;
--null인경우 0표시
select nvl(department_id,0)from employees;
--null인경우 CEO표시
select nvl(to_char(department_id),'CEO')from employees;

----------그룹함수

--sum 합계,avg 평균,count 개수,min 최소값,max 최대값,median 중간값
select salary from employees;

select sum(salary) from employees;
select to_char(sum(salary),'999,999') from employees;

select avg(salary) from employees;
--소수점 4자리 반올림 / 내림
select round(avg(salary),4) from employees;
select trunc(avg(salary),4) from employees;
--최대값 최소값
select max(salary) from employees;
select min(salary) from employees;

--평균값보다 월급이 높은 사원을 출력
select avg(salary) from employees;
--1.
select count(salary) from employees
where salary >=6461.83;
--2.
select count(salary) from employees
where salary >=(select avg(salary) from employees);

--emp_name 단일함수, avg 그룹함수 같이 쓸수없음
select emp_name,avg(salary) from employees;
--단일함수 그룹함수 함께 사용할수없음
select department_id,max(salary) from employees;

--students 테이블 모든학생의 kor 점수 합계 평균 최대값 최소값을 구하시오
select kor from students;

select sum(kor),avg(kor),max(kor),min(kor),median(kor) from students;


-- 부서번호가 50인 사원들의 월급의 합 평균 최대값 최소값을 출력
select sum(salary),avg(salary),max(salary),min(salary),median(salary) from employees
where department_id =50;

select max(salary) from employees
where department_id =50;
-- group by 단일함수를 출력하고 싶을때 단일함수를 입력하면됨
select department_id,max(salary) from employees
group by department_id;

select emp_name,salary from employees;
--107명의 평균
select avg(salary) from employees;
--단일 함수 그룹함수 함께 사용하려면 group by 지정
select department_id,round(avg(salary),2),count(salary),max(salary),min(salary) from employees
group by department_id order by department_id;

--평균 월급보다 높은사람 수를 출력하시오
select count(salary),min(salary),max(salary) from employees
where salary>= (select avg(salary) from employees);

--수학함수
-- abs 절대값 ceil 올림 floor 내림 round 반올림 trunc 절사 mod 나머지 power 제곱 sqrt 제곱근
-- 제곱
select power(2,3),2*2*2 from dual;

-- 문자,숫자형 > 날짜형타입 변경가능
--숫자,날짜형타입 > 문자형타입 변경가능
--문자형 타입 > 숫자형 타입 변경가능

select 20240101,to_date(20240101) from dual;
--날짜형타입 > 숫자형타입 변경불가(형태를 변경해서 문자형으로 변경 후 숫자형으로 변경가능)
select sysdate,to_number(sysdate) from dual;

select '2',to_number('2') from dual;

select '20240101',to_number('20240101') from dual;

--날짜 > 문자 > 숫자
select sysdate,to_number(to_char(sysdate,'yyyymmdd')) from dual;

-- 날짜형타입을 문자형타입으로 변경시,  년 월 일 한글입력방법
select sysdate,to_char(sysdate,'yyyy"년"mm"월"dd"일" day') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd day') from dual;



----문자형함수

select emp_name,email from employees;
--문자형타입을 합치려고 +기호 사용하면 에러
select emp_name+email from employees;

--|| concat함수
select emp_name||email from employees; -- 속도가 더빠름
select concat(emp_name,email) from employees;
--숫자형타입 :사칙연산 계산해서 출력됨
select kor+eng from students;


--'john'  소문자취환 upper 대문자 취환 initcap 첫글자 대문자취환
select * from member
where lower(name)= 'bryan';

select 'john',initcap('john'),lower('john'),upper('john') from dual;

--lpad() 왼쪽 자리수 채우기 
select 'john',lpad('john',10,'#') from dual;

--rpad() 오른쪽 자리수 채우기
select 'john',rpad('john',10,'#') from dual;

-- trim :d앞 뒤 공백없애기 ltrim 왼쪽공백없애기 rtrim 오른쪽공백없애기
select length('   aaa   '),length(trim('   aaa   ')) from dual;

--replace 취환
select '  a b c  ',trim('  a b c  ') from dual;

select '  a b c  ',trim('  a b c  '),length(replace('  a b c  ',' ','')) from dual;

--substr 특정위치 자르기(시작위치 ,개수)
select 'abcedfg',substr('abcedfg',0,3),substr('abcedfg',3,2) from dual;

--입사일이 3월인 사원을 출력
select emp_name,hire_date from employees
where substr(hire_date,4,2)='03';

select emp_name,hire_date from employees
where substr(hire_date,4,2) in ('03','08','10');
--7월 이상
select emp_name,hire_date from employees
where substr(hire_date,4,2) >= 7;

--translate 취환('xy','ab'):x는 a로 y는b로 취환
--replace 취환('xy','ab'):xy는 ab로 취환
--순서에 없는 변환글자는 삭제 처리(k)
select 'axyz',translate('axyzxk','xyk','ab')from dual;
select 'axyz',replace('axyzx','xy','ab')from dual;

--length() : 문자열길이
--students테이블 name 글자길이가 5자이상인 학생만 출력하시오
select name,length(name) from students
where length(name)>= 10;
select count(*) from students
where length(name)>= 10;

--사원의 월급의 합과 평균 구하기
select sum(salary),avg(salary) from employees;

--영어점수의 합과 평균 최대값 최소값 구하기
select sum(eng),avg(eng),max(eng),min(eng) from students;

--students 테이블에서  '홍길동' 등록일 2023년12월02일
select name,to_char(sdate,'"등록일" yyyy"년"mm"월"dd"일" day')from students




