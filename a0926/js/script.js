let count =1;   //전역변수 - 회원번호 변수
let total =0;  //전역변수 -합계변수
let avg =0;  //전역변수 -평균변수
let id_num;  //전역변수 -현재위치 확인변수
let temp = 0; //수정버튼 클릭 확인 변수
let tr_this;
$(function(){
  //1.ajax 데이터 가져오기
$.ajax({
  url:"js/stuData.json",
  type:"get",
  data:"",
  dataType:"json",
  success:function(data){
    console.log(data);
    let s_data ="";
    for(var i=0;i<data.length;i++){
      count++
      total = data[i].kor+data[i].eng+data[i].math;
      avg = (total/3).toFixed(2);

      s_data += `<tr id="${i+1}">`
      s_data += `<td>${data[i].no}</td>`
      s_data += `<td>${data[i].name}</td>`
      s_data += `<td>${data[i].kor}</td>`
      s_data += `<td>${data[i].eng}</td>`
      s_data += `<td>${data[i].math}</td>`
      s_data += `<td>${total}</td>`
      s_data += `<td>${avg}</td>`
      s_data += `<td><button class="updateBtn">수정</button>
                <button class="delBtn">삭제</button></td>`
      s_data +=  `</tr>`
    }
    $("#tbody").html(s_data);
    
    //삭제
    $(document).on("click",".delBtn",function(){
      console.log($(this).closest("tr").attr("id"));
      let id_num = $(this).closest("tr").attr("id");
      if(confirm(id_num+"번의 학생 성적을 삭제하시겠습니까?")){
        $("#"+id_num).remove();
        alert(id_num+"번의 학생성적이 삭제되었습니다");
      }
    });
  },
  error:function(){
    alert("실패");
  }
  
  
  
})//ajax

//입력
$(document).on("click","#create",function(){
  let name = $("#name").val();
  let kor = Number($("#kor").val());
  let eng = Number($("#eng").val());
  let math = Number($("#math").val());
  let total = kor+eng+math;
  let avg = (total/3).toFixed(2);
   //입력한 데이터 있는지 확인
  if($("#name").val().length<1 ||$("#kor").val().length<1 ||$("#eng").val().length<1 ||$("#math").val().length<1){
    alert("이름 및 점수를 입력하셔야 저장이 가능합니다.");
    return false;
  }
  alert(name+"학생성적을 저장합니다.");
  
  let s_data ="";
  
  s_data += `<tr id="${count}">`
  s_data += `<td>${count}</td>`
  s_data += `<td>${name}</td>`
  s_data += `<td>${kor}</td>`
  s_data += `<td>${eng}</td>`
  s_data += `<td>${math}</td>`
  s_data += `<td>${total}</td>`
  s_data += `<td>${avg}</td>`
  s_data += `<td><button class="updateBtn">수정</button>
  <button class="delBtn">삭제</button></td>`
  s_data +=  `</tr>`
  $("#tbody").prepend(s_data); //append 아래추가
  count++
  //입력한값삭제
  $("#name").val("");
  $("#kor").val("");
  $("#eng").val("");
  $("#math").val("");
  
})

//수정
$(document).on("click",".updateBtn",function(){
  
  //수정버튼 클릭이 되어있는지 확인
  if(temp==1){
    alert("수정완료 또는 수정취소 버튼을 먼저 클릭하셔야합니다.");
    return false;
  }
  tr_this = this;
  $(this).css({"color":"red","font-weight":"600"})

  alert("수정을 진행합니다.");
  let id_num = $(this).closest("tr").attr("id");
  $("#create,#update,#updateCancel").toggle();
  temp=1;

  let u_data = $(this).closest("tr");
  console.log(u_data.children("td:eq(1)").text());
  console.log(u_data.children("td:eq(2)").text());
  console.log(u_data.children("td:eq(3)").text());
  console.log(u_data.children("td:eq(4)").text());

  $("#name").val(u_data.children("td:eq(1)").text());
  $("#kor").val(u_data.children("td:eq(2)").text());
  $("#eng").val(u_data.children("td:eq(3)").text());
  $("#math").val(u_data.children("td:eq(4)").text());

});
//수정완료
$(document).on("click","#update",function(){
tr_this.css({"color":"black","font-weight":"400"});
let name = $("#name").val();
let kor = Number($("#kor").val());
let eng = Number($("#eng").val());
let math = Number($("#math").val());
let total = kor+eng+math;
let avg = (total/3).toFixed(2)
//입력한 데이터가 있는지확인
if($("#name").val().length<1||$("#kor").val().length<1||$("#eng").val().length<1||$("#math").val().length<1){
alert("이름 및 점수를 입력하셔야 수정이 가능합니다.");
return false;}
//차트안에 넣기
console.log("수정완료 버튼 클릭 id_num: "+id_num);

let s_data ="";
s_data += `<td>${id_num}</td>`
s_data += `<td>${name}</td>`
s_data += `<td>${kor}</td>`
s_data += `<td>${eng}</td>`
s_data += `<td>${math}</td>`
s_data += `<td>${total}</td>`
s_data += `<td>${avg}</td>`
s_data += `<td>
  <button class='updateBtn'>수정</button>
  <button class='delBtn'>삭제</button>
  </td>`;

$("#"+id_num).html(s_data);
count++
$("#name").val("");
$("#kor").val(""); 
$("#eng").val("");  
$("#math").val(""); 

alert("수정이 되었습니다.");
$("#create,#update,#updateCancel").toggle();
temp=0;
})
//수정취소
$(document).on("click","#updateCancel",function(){
tr_this.css({"color":"black","font-weight":"400"});

alert("수정이 취소 되었습니다");
$("#create,#update,#updateCancel").toggle();
//데이터 지우기
$("#name").val("");
$("#kor").val("");
$("#eng").val("");
$("#math").val("");
temp=0;
});

});//jquery