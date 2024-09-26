//jquery 선언
let num=0;
let num2=0;
$(function(){
  //우측버튼
 $("#right").click(function(){
   //alert("우측버튼 클릭");
   if(num>=900){
     alert("오른쪽끝에 도달");
     return false;
    }
   $("#box").stop();
   num += 100;
   num2 += 360;
   $("#box").animate({
    left:num,"rotate":num2+"deg"
   },1000);
  
 });
 //좌측버튼
 $("#left").click(function(){
   //alert("좌측버튼 클릭");
   if(num<=0){
     alert("왼쪽끝에 도달했습니다. 좌측이동불가");
     return false;
    }
   $("#box").stop();
   num -= 100;
   num2 -= 360;
   $("#box").animate({
    left:num,"rotate":num2+"deg"
   },1000);
 });
});jquery