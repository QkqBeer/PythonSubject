document.write("<script language='JavaScript' src='three.js'></script>");
document.write("<script language='JavaScript' src='ThreeBSP.js'></script>");
document.write("<script language='JavaScript' src='action.js'></script>");
document.write("<script language='JavaScript' src='OrbitControls.js'></script>");
document.write("<script language='JavaScript' src='TrackballControls.js'></script>");

//加载xml文件，根据浏览器的不同返回不一样的对象
loadXML = function (file) {
    console.log('欢迎来到那位先生三维空间，施展你的才华吧！邮箱地址：614129067@qq.com');
    var xmlDoc;
    try {
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
    }
    catch (e) {
        try {
            var XmlHttp = new XMLHttpRequest();
            XmlHttp.open("GET", file, false);
            XmlHttp.send(null);
            xmlDoc = XmlHttp.responseXML;
            return xmlDoc;
        } catch (e) {
            return;
        }
    }
    xmlDoc.async = false;
    xmlDoc.load(url);
    return xmlDoc;
};
//程序入口处
checkXMLDocObj = function (xmlFile) {
    var xmlDoc = loadXML(xmlFile);
    if (xmlDoc == null) {
        console.log('你的浏览器不支持xml文件的读取')
    }
    return xmlDoc;
};


//遍历一棵树
xmlParserBuildTree = function (xmlDoc) {
    var EventGraph = [];
    var rootChildElement = xmlDoc.getElementsByTagName('Graph')[0].children;
    var rootElement = xmlDoc.getElementsByTagName('Graph')[0];
    var scene = initScene();
    //光源
    var ambientLight = new THREE.AmbientLight(0x0c0c0c);
    scene.add(ambientLight);


    var Light = initLight(rootElement.getAttribute('light'));
    scene.add(Light);

    var camera;
    //相机
    camera = initCam(rootElement.getAttribute('camera'), scene.position);
    var renderer;
    //渲染器
    renderer = initRenderer(rootElement.getAttribute('renderer'));

    for (var i = 0; i < rootChildElement.length; i++) {
        var objList;
        if (rootChildElement[i].nodeName == 'complexGraph') {
            objList = drawComplexGraph(rootChildElement[i]);
        }
        else if (rootChildElement[i].nodeName == 'cube') {
            objList = drawCube(rootChildElement[i]);
        }
        else if (rootChildElement[i].nodeName == 'sphere') {
            objList = drawSphere(rootChildElement[i])
        }
        else if (rootChildElement[i].nodeName == 'plane') {
            objList = drawPlane(rootChildElement[i]);
        }
        scene.add(objList.obj);
        EventGraph.push(objList);
    }
    //声明鼠标控制controls
    var MouseControls = clearControls(camera);
    //绑定拖拽事件监听器
    bindingDragListener(renderer, scene, camera, EventGraph, MouseControls);
    //给窗口绑定单击监听事件
    bindingListener(renderer, scene, camera, EventGraph);

    return {'renderer': renderer, 'camera': camera, 'scene': scene, 'controls':MouseControls}
};

initScene = function (){
    var scene = new THREE.Scene();
    return scene;
};


initCam = function (attr, position) {
    var camera;
    if (attr == 'PerspectiveCamera') {
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.x = -30;
        camera.position.y = 50;
        camera.position.z = 30;
        camera.lookAt(position);
    }
    return camera;
};

initRenderer = function (attr) {
    var renderer;
    if (attr == 'WebGLRenderer') {
        var renderer = new THREE.WebGLRenderer();
        renderer.setClearColor(0xEEEEEE, 1.0);
        renderer.antialias = true;
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMapEnabled = true;
        //是否排列对象 默认是true
        renderer.sortObjects = false;
        //设置渲染的范围
        //设置阴影地图是纹理阴影
        renderer.shadowMapType = THREE.PCFShadowMap;
    }
    else if (attr.nodeValue == 'CanvasRenderer') {

    }
    return renderer
};
//平面
drawPlane = function (node) {
    var position = node.getAttribute('position').split(',');
    var material = initMaterial(node.getAttribute('material'));
    var size = node.getAttribute('size').split(',');
    //var planeGeometry = new THREE.PlaneGeometry(parseInt(size[0]), parseInt(size[1]),3,3);
    var planeGeometry = new THREE.PlaneGeometry(20, 20, 3, 3);
    var plane = new THREE.Mesh(planeGeometry, material);
    plane.position.x = parseInt(position[0]);
    plane.position.y = parseInt(position[1]);
    plane.position.z = parseInt(position[2]);
    plane.castShadow = true;
    return ParseChildelement(node.children, plane);
};

//正方体，长方体
drawCube = function (node) {
    var position = node.getAttribute('position').split(',');
    var material = initMaterial(node.getAttribute('material'));
    var size = node.getAttribute('size').split(',');
    var cubeGeometry = new THREE.CubeGeometry(parseInt(size[0]), parseInt(size[1]), parseInt(size[2]), 1, 1, 1);
    var cube = new THREE.Mesh(cubeGeometry, material);
    cube.position.x = parseInt(position[0]);
    cube.position.y = parseInt(position[1]);
    cube.position.z = parseInt(position[2]);
    cube.castShadow = true;
    return ParseChildelement(node.children, cube);
};
//复合图形
drawComplexGraph = function (node) {
    var style = node.getAttribute('style');
    var childElement = node.children;
    var obj;
    var newChildList = [];
    for (var i = 0; i < childElement.length; i++) {
        if (childElement[i].nodeName == 'cube') {
            obj = drawCube(childElement[i]).obj;
        }
        else if (childElement[i].nodeName == 'sphere') {
            obj = drawSphere(childElement[i]).obj;
        }
        else if (childElement[i].nodeName == 'complexGraph') {
            obj = drawComplexGraph(childElement[i]).obj;
        }
        newChildList.push(obj);
    }
    var resultBSP;
    var mainThreeBSP = new ThreeBSP(newChildList[0]);
    switch (style) {
        case "subtract":
            for (var j = 1; j < newChildList.length; j++) {
                resultBSP = mainThreeBSP.subtract(new ThreeBSP(newChildList[j]))
            }
            break;
        case "intersect":
            for (var j = 1; j < newChildList.length; j++) {
                resultBSP = mainThreeBSP.intersect(new ThreeBSP(newChildList[j]))
            }
            break;
        case "union":
            for (var j = 1; j < newChildList.length; j++) {
                resultBSP = mainThreeBSP.union(new ThreeBSP(newChildList[j]))
            }
            break;
        case "none":
    }

    var result = resultBSP.toMesh();
    result.geometry.computeFaceNormals();
    result.geometry.computeVertexNormals();
    //在复合图形中没有detail
    var len = node.children.length;
    var complexGraph;
    if (node.children[len - 1].nodeName == 'Event') {
        complexGraph = ParseChildelement([node.children[len - 1]], result);
    }
    else {
        complexGraph = new ActionGraph(result);
    }
    return complexGraph;
};
//球体
drawSphere = function (node) {
    var position = node.getAttribute('position').split(',');
    var radius = node.getAttribute('radius');
    var material = initMaterial(node.getAttribute('material'));
    var sphereGeometry = new THREE.SphereGeometry(parseInt(radius), 25, 25);
    var sphere = new THREE.Mesh(sphereGeometry, material)
    sphere.position.x = parseInt(position[0]);
    sphere.position.y = parseInt(position[1]);
    sphere.position.z = parseInt(position[2]);
    sphere.castShadow = true;

    return ParseChildelement(node.children, sphere);
};

//初始化材料
initMaterial = function (type) {
    var Material;
    if (type == 'MeshLambertMaterial') {
        Material = new THREE.MeshLambertMaterial()
    }
    else if (type == 'MeshNormalMaterial') {
        Material = new THREE.MeshNormalMaterial();
        Material.side = THREE.DoubleSide;
    }
    else if (type == 'MeshBasicMaterial') {
        Material = new THREE.MeshBasicMaterial();

    }
    return Material
};

initLight = function (type) {
    var Light;
    if (type == 'SpotLight') {
        Light = new THREE.SpotLight(0xffffff);
        Light.position.set(-40, 60, -10)
        Light.castShadow = true
    }
    return Light;
};

//解析图形的子标签events和detail
ParseChildelement = function (element, obj) {
    var childElement = element;
    var newObj;
    var detailObj;
    var flagEvent = false;
    var flagDetail = false;
    for (var i = 0; i < childElement.length; i++) {
        //绑定交互事件
        if (childElement[i].nodeName == 'Event') {
            flagEvent = true;
            newObj = bindingEvents(obj, childElement[i]);
        }
        else if (childElement[i].nodeName == 'Detail') {
            //返回的还是一个图形对象
            flagDetail = true;
            detailObj = drawDetail(obj, childElement[i]);
        }
    }
    if (flagEvent) {

    }
    else {
        newObj = new ActionGraph(obj);
    }
    if (flagDetail) {
        newObj.obj = detailObj;
    }
    return newObj
};


//不同的图形有可能不需要某些特定事件或者需要某些事件，绑定交互事件。
bindingEvents = function (obj, events) {
    var eventList = events.children;
    var EventObj = new ActionGraph(obj);

    for (var i = 0; i < eventList.length; i++) {
        var className = eventList[i].getAttribute('class');
        var eventName = eventList[i].getAttribute('eventName');
        if (className == 'mouse') {
            if (eventName == 'click') {
                EventObj.event.push('click');
            }
            else if (eventName == 'doubleClick') {
                EventObj.event.push('doubleClick');
            }
        }
        else if (className == 'keyboard') {

        }
        else if (className == 'gesture') {

        }
        else {

        }
    }

    return EventObj
};

//绘制细节
drawDetail = function (obj, detail) {
    var segments = detail.getAttribute('segments').split(',');
    var func = detail.getAttribute('function');
    var radian = detail.getAttribute('radian');
    var pel = detail.getAttribute('pel');
    console.log(obj);
    drawDetailSegment(obj, segments);
    console.log(obj);
    return obj;
};
drawDetailSegment = function (obj, segments){
    if (segments.length == 2) {
        obj.geometry.parameters.widthSegments = parseInt(segments[1]);
        obj.geometry.parameters.heightSegments = parseInt(segments[0]);
    }
    else {
        obj.geometry.parameters.depthSegments = parseInt(segments[0]);
        obj.geometry.parameters.heightSegments = parseInt(segments[1]);
        obj.geometry.parameters.widthSegments = parseInt(segments[2]);
    }
};

//绑定监听器
bindingListener = function (renderer, scene, camera, EventGraph) {
    //单击监听器
    bindingClickListener(renderer, scene, camera, EventGraph);
};


//绑定单击事件
bindingClickListener = function (renderer, scene, camera, EventGraph) {
    //声明raycaster和mouse变量
    var raycaster = new THREE.Raycaster();
    var mouse = new THREE.Vector2();
    //单击监听器
    renderer.domElement.addEventListener('click', function (event) {
            //通过鼠标点击的位置计算出raycaster所需要的点的位置，以屏幕中心为原点，值的范围为-1到1.
            mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
            mouse.y = -( event.clientY / window.innerHeight ) * 2 + 1;
            // 通过鼠标点的位置和当前相机的矩阵计算出raycaster
            raycaster.setFromCamera(mouse, camera);
            // 获取raycaster直线和所有模型相交的数组集合
            var intersects = raycaster.intersectObjects(scene.children);
            //将所有的相交的模型的颜色设置为红色，如果只需要将第一个触发事件，那就数组的第一个模型改变颜色即可
            for (var i = 0; i < intersects.length; i++) {
                for (var j = 0; j < EventGraph.length; j++) {
                    if (intersects[i].object.uuid == EventGraph[j].obj.uuid) {
                        var changeObj = ActionGraph(intersects[i]);
                        for (var k = 0; k < EventGraph[j].event.length; k++) {
                            if (EventGraph[j].event[k] == 'click') {
                                ActionGraph.mouseClick(EventGraph[j]);
                            }
                        }
                    }
                }
            }
        }
    );
};


//声明鼠标控制
clearControls = function (camera){
    var controls,
    //设定一系列控制参数。
    controls = new THREE.TrackballControls(camera);
    //旋转速度
    controls.rotateSpeed = 1.0;
    //变焦速度
    controls.zoomSpeed = 1.2;
    //平移速度
    controls.panSpeed = 0.8;
    //是否不变焦
    controls.noZoom = false;
    //是否不平移
    controls.noPan = true;
    //可能是惯性 true没有惯性
    controls.staticMoving = false;
    //动态阻尼系数 就是灵敏度
    controls.dynamicDampingFactor = 0.3;
    return controls
};

//声明鼠标拖拽
bindingDragListener = function (renderer, scene, camera, EventGraph, controls) {
    //projector是可能指屏幕和场景转换工具 renderer是指场景渲染，能把场景呈现到浏览器里
    var projector;
    //objects是指场景中的实体集合  plane是一个水平面网格，当选中一个物体时，可以通过这个水平面，看到和它在同一平面内的其他物理
    var objects = [], plane;
    //mouse，鼠标所对应的二维向量  offset 是指三维偏移向量 INTERSECTED是指相交的对象 SELECTED选中的对象
    var mouse = new THREE.Vector2(),
        offset = new THREE.Vector3(),
        INTERSECTED, SELECTED;


    for (var i = 0; i < EventGraph.length; i++) {
        objects.push(EventGraph[i].obj)
    }
    //创建一个长2000宽2000，8*8的网格对象并加上一种基本材质
    plane = new THREE.Mesh(new THREE.PlaneGeometry(2000, 2000), new THREE.MeshBasicMaterial({
        color: 0x000000,
        opacity: 0.25,
        transparent: true,
        wireframe: true
    }));
    //网格对象是否可见
    plane.visible = true;
    //把网格对象加到场景中
    scene.add(plane);

    //创建一个屏幕和场景转换工具
    projector = new THREE.Projector();
    //加入鼠标拖动对象的一系列监听事件
    renderer.domElement.addEventListener('mousemove', function (event) {
        //阻止本来的默认事件，比如浏览器的默认右键事件是弹出浏览器的选项
        event.preventDefault();
        //mouse.x是指 鼠标的x到屏幕y轴的距离与屏幕宽的一半的比值 绝对值不超过1
        //mouse.y是指 鼠标的y到屏幕x轴的距离与屏幕宽的一半的比值 绝对值不超过1
        //
        //下面的矩形是显示器屏幕，三维空间坐标系的布局以及屏幕的二维坐标系
        //
        // 鼠标是从  二维坐标系
        // 这个点 .-------------------------------------------|-->鼠标x正半轴
        //  开始算|                   个 y     /              |
        //   x,y  |                    |     /                |
        //        |                    |   /                  |
        //        |          三维坐标系 | /                    |
        //        | -------------------/-------------------->x|
        //        |                  / |                      |
        //        |                /   |                      |
        //        |              /     |                      |
        //        |__________Z_匕______|______________________|
        //        |
        // 鼠标y  \/
        // 正半轴
        mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
        mouse.y = -( event.clientY / window.innerHeight ) * 2 + 1;

        //新建一个三维变换半单位向量 假设z方向就是0.5,这样我左右移的时候，还会有前后移的效果
        var vector = new THREE.Vector3(mouse.x, mouse.y, 0.5);

        //屏幕和场景转换工具根据照相机，把这个向量从屏幕转化为场景中的向量
        projector.unprojectVector(vector, camera);

        //新建一条从相机的位置到vector向量的一道光线
        var raycaster = new THREE.Raycaster(camera.position, vector.sub(camera.position).normalize());

        //是否有东西被选中
        if (SELECTED)
        {
            //有的话取到这条光线射到的物体所在水平面上所有相交元素的集合,所以这样就可以限制每次拖动距离不能超出水平面panel
            var intersects = raycaster.intersectObject(plane);
            //这个鼠标点中的点的位置减去偏移向量，新位置赋值给选中物体
            if (intersects.length > 0)
            {
                SELECTED.position.copy(intersects[0].point.sub(offset));
            }
            return;
        }

        //否则的话，光线和所有物体相交，返回相交的物体
        var intersects = raycaster.intersectObjects(objects);
        //如果有物体相交了
        if (intersects.length > 0)
        {
            //并且相交物体不是上一个相交物体
            if (INTERSECTED != intersects[0].object)
            {
                //将这个对象放到INTERSECTED中
                INTERSECTED = intersects[0].object;
                //改变水平面的位置
                plane.position.copy(INTERSECTED.position);
                //并把水平面指向到相机的方向
                plane.lookAt(camera.position);

            }
        }
    }, false);
    renderer.domElement.addEventListener('mousedown', function (event) {
        //阻止本来的默认事件，比如浏览器的默认右键事件是弹出浏览器的选项
        event.preventDefault();
        var vector = new THREE.Vector3(mouse.x, mouse.y, 0.5);
        projector.unprojectVector(vector, camera);

        var raycaster = new THREE.Raycaster(camera.position, vector.sub(camera.position).normalize());

        var intersects = raycaster.intersectObjects(objects);

        if (intersects.length > 0)
        {
            //不能改变视角了
            controls.enabled = false;
            //把选中的对象放到全局变量SELECTED中
            SELECTED = intersects[0].object;
            //再和水平面相交
            var intersects = raycaster.intersectObject(plane);

            //选中位置和水平面位置（物体中心）的偏移量
            offset.copy(intersects[0].point).sub(plane.position);
        }
    }, false);
    renderer.domElement.addEventListener('mouseup', function (event) {
        event.preventDefault();
        //又能改变视角了
        controls.enabled = true;
        //如果有相交物体
        if (INTERSECTED)
        {
            //把位置给水平面
            plane.position.copy(INTERSECTED.position);
            //选中物体置空
            SELECTED = null;
        }

    }, false);

    //加入窗口改变大小时的监听事件
    window.addEventListener('resize', function(){
        //改变相机的aspect属性为当前窗口的宽高
        camera.aspect = window.innerWidth / window.innerHeight;
        //更新相机的投影矩阵
        camera.updateProjectionMatrix();
        //重新设置场景宽高
        renderer.setSize(window.innerWidth, window.innerHeight);
    }, false);
};


