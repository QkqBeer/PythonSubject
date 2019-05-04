document.write("<script language='JavaScript' src='three.js'></script>");
function ActionGraph(obj){
    this.obj = obj;
    this.event = new Array();
}

ActionGraph.mouseClick = function(obj){
    //做异常检测
   try{
       obj.obj.material.color.set(0xff0000);
   }
   catch (error)
   {
       var newMaterial = new THREE.MeshBasicMaterial({color:0xffffff});
       obj.obj.material = newMaterial;
   }
};
ActionGraph.mouseDoubleClick = function(obj){


};
ActionGraph.leftSlide = function(obj){
    obj.object.material.color.set(0xff0000);
};