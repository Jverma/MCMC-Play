function drawLine(svg, data, m, c, x, y){
	var new_data = data.map(function(d){
	  	return {'x': d.x, 'y': m * d.x + c};
	  });
	// console.log("draw line");

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



function drawParabola(svg, data, a, b, c, x, y){
	var new_data = data.map(function(d){
		return {'x': d.x, 'y': a * Math.pow(d.x, 2) + b * d.x + c};
	});

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