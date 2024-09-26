$(function(){

  $("#searchBtn").click(function(){
    alert("검색버튼 클릭")
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=rVpu5F6M71Yaz4YLIaDwxtcZUdsnNJNXMmuUnYoVO48t0woxPlmL7Zl3KWV5llyv90RtZJXyyFgJfoLJ0fg0Gg%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    $.ajax({
      url:surl,
      type:"get",
      data:"",
      dataType:"json",
      success:function(data){
       alert("성공");
       let a_data ="";
       let s_data = data.response.body.items.item;
       console.log(data.response.body.items.item);
       for(var i=0;i<s_data.length;i++){
        //console.log(s_data[i].galContentId);
        a_data += `<tr>`
        a_data += `<td>${s_data[i].galContentId}</td>`
        a_data += `<td>${s_data[i].galTitle}</td>`
        a_data += `<td>${s_data[i].galPhotographer}</td>`
        a_data += `<td>${s_data[i].galCreatedtime}</td>`
        a_data += `<td><img src= ${s_data[i].galWebImageUrl}></td>`
        a_data += `</tr>`
       }
      $("#tbody").html(a_data);
      },
      error:function(){
       alert("실패");
      }
      
    })//ajax
  })//searchBtn
})//jquery