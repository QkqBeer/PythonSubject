PlaneGeometry1 = function (width, height, segmentsWidth, segmentsHeight)
{
     THREE.Geometry.call(this)
    //计算，我们需要哪些顶点来构成面
    var ix, iz
    width_half = width / 2
    height_half = height / 2
    gridX = segmentsWidth || 1
    gridZ = segmentsHeight || 1

    segments_Width = width / gridX
    segments_Height = height / gridZ

    normal = new THREE.Vector3(0, 0, 1)
    //要将顶点的顺序给传递出去
    //给与我们实现平面一些纹理坐标
    for(iz = 0; iz <= gridX; iz++){
         for(ix = 0; ix <= gridX; ix++){
             var x = -width_half + ix * segments_Width;
             var y = -height_half + iz * segments_Height;
             this.vertices.push(x, -y, 0)
         }
    }

    //x要将顶点的顺序给传递进去，new Face4()
    for(iz = 0; iz < gridZ; iz++){
        for(ix = 0; ix < gridX; ix++){
            var a = ix + (gridX + 1) * iz;
            var b = ix + (gridX + 1) * iz;
            var c = (ix + 1) + (gridX + 1) * (iz + 1);
            var d = (ix + 1) + (gridX + 1) * iz;
            var face = new THREE.Face4(a,b,c,d);
            face.normal.copy(normal);
            face.vertexNormals.push(normal.clone(),normal.clone(),normal.clone(),normal.clone())
            this.faces.push(face)
        }
    }
    //给与我们实现平面一些纹理坐标
    //计算这个面的重心
    //this.computeCentroids()
}
PlaneGeometry1.prototype = Object.create(THREE.Geometry.prototype)