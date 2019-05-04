var canvas=document.getElementById('canvas');
context=canvas.getContext('2d');


//实体字
// context.font='38pt Arial';
// context.fillStyle='cornflowerblue';
// context.fillText('hello canvas',canvas.height/2-150,canvas.height/2+15)

//空心字
// context.strokeStyle='blue';
// context.strokeText('hello canvas',canvas.width/2-150,canvas.height/2+15)


//画圆
// function drawCircle() {
//     context.beginPath();
//     context.arc(canvas.width/2,canvas.height/2,100,0,Math.PI*2,true)
//     context.stroke()
// }
// function drawNumerals() {
//     var numerals=[1,2,3,4,5,6,7,8,9,10,11,12]
//     angle=0
//     numeralWidth=0
//     numerals.forEach(function (numeral) {
//         angle=Math.PI/6*(numeral-3)
//         numeralWidth=context.measureText(numeral).width;
//         context.fillText(numeral,
//             canvas.width/2 + Math.cos(angle)*(120)-numeralWidth/2,
//             canvas.height/2 + Math.sin(angle)*(120)-15/3)
//     })
// }
//
// drawCircle()
// drawNumerals()


//放大镜
canvas = document.getElementById('canvas');
context = canvas.getContext('2d');
rubberbandiv = document.getElementById('rubberbandiv');
rectangle = {};
image = new Image();
image.src='1.jpg';
var dragging = false;
image.onload = function(e){
    context.drawImage(image,0,0)
};
canvas.onmousedown = function(e){
    var x = e.clientX,y= e.clientY;
    e.preventDefault();
    rubberbandstart(x,y);//开始截图图
};
window.onmousemove = function(e){
    var x = e.clientX,y= e.clientY;
    e.preventDefault();
    rubberbandstrech(x,y);//鼠标移动的距离
};

window.onmouseup = function(e){
    rubberbandend();//截图结束
};
function rubberbandstart(x,y){
    mounsedownx =x;
    mounsedowny = y;//get indexod x,y
    rectangle.left = mounsedownx;
    rectangle.top =mounsedowny;
    moveRubberbanddiv();//定义选取框的起点
    showRubberbanddiv();
    dragging = true;
}
function moveRubberbanddiv(){
    rubberbandiv.style.top = rectangle.top + 'px';
    rubberbandiv.style.left = rectangle.left + 'px';
}
function showRubberbanddiv(){
    rubberbandiv.style.display = 'inline'
}
function rubberbandstrech(x,y){
    rectangle.left = x<mounsedownx?x:mounsedownx;
    rectangle.top = y<mounsedowny?y:mounsedowny;
    rectangle.width = Math.abs(x-mounsedownx) ;
    rectangle.height = Math.abs(y-mounsedowny);
    moveRubberbanddiv();//当移动的点在mounsedown的左边时，要从新定义left，top(选取框的起点)
    resizeRubberbanddiv();//
}
function resizeRubberbanddiv(){
    rubberbandiv.style.width = rectangle.width +'px';
    rubberbandiv.style.height = rectangle.height +'px';
}

function rubberbandend(){
    var bbox = canvas.getBoundingClientRect();
    try{
        context.drawImage(canvas,rectangle.left-bbox.left,rectangle.top-bbox.top,rectangle.width,rectangle
            .height,0,0,canvas.width,canvas.height);
        //查看图片1.png 了解参数详情
    }
    catch (e){

    }
    resetRubberbandRectangle();
    rubberbandiv.style.width = 0;
    rubberbandiv.style.height = 0;
    hideRubberbanddiv();
    dragging =false;
}
function resetRubberbandRectangle(){
    rectangle = {top:0,left:0,width:0,height:0};
}
function hideRubberbanddiv(){
    rubberbandiv.style.display = 'none';
}
