function drawLine(svg, data, m, c, x, y){
	var new_data = data.map(function(d){
	  	return {'x': d.x, 'y': m * d.x + c};
	  });
	console.log("draw line");

	var line = d3.svg.line()
	    .x(function(d) { return x(d.x); })
	    .y(function(d) { return y(d.y); });

	svg.select(".line")
		.remove();

  	svg.append("path")
      .datum(new_data)
      .attr("class", "line")
      .attr("d", line);
}