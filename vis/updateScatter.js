function update(svg, data, x, y, xAxis, yAxis){
  // x.domain(d3.extent(data, function(d) { return d.x; })).nice();
  // y.domain(d3.extent(data, function(d) { return d.y; })).nice();

  // alert(x(1.0));

  // console.log("draw scatterplot");

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", -6)
      .style("text-anchor", "end")
      .text("X");


  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Y");

  var scatter = svg.selectAll(".dot")
      .data(data);

  scatter.attr("class", "update")
    .transition()
    // .delay(500);
      .duration(750);
      // .attr("x", function(d, i) { return i * 32; });


  scatter.enter().append("circle")
      .attr("class", "enter")
      .attr("r", "2.5")
      .attr("cx", function(d) { return x(d.x); })
      .attr("cy", function(d) { return y(d.y); })
      .style("fill-opacity", 1e-6)
    .transition()
      .duration(750)
      .style("fill-opacity", 1);

  scatter.exit()
      .attr("class", "exit")
    .transition()
      .duration(750)
      .style("fill-opacity", 1e-6)
      .remove();
};


// function drawLine(svg, slope, intercept, x, y){
//   svg.append("line")
//     .attr("x1", x(slope))
//     .attr("y1", y(0))
//     .attr("x2", x(slope))
//     .attr("y2", y(intercept))
//     .attr("stroke-width", 2)
//     .attr("stroke","blue");
// }

// function alpha(data, x, time){
//   setInterval(function(){
//   data.push(x);
// }, time);
// }

// function MCMC(data){
//   for (i=0; i<100; i++){
//     var num = {'x': Math.random(), 'y': Math.random()}
//     data.push(num);
//     // alpha(data, num, 500);
//   }
// }

