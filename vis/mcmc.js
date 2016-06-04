/*
MCMC - Metropolis Hastings algorithm in JavaScript.
@author - jverma
Created on - 05/12/2016
*/

// Initialize the Markov chain.
function initialize(num_params, min_params, max_params){
	/*
	Params
	-------
	num_params: Integer, number of parameters.
	Default is 2.
	min_params: Array, minimum values of the parameters.
	max_params: Array, maximum values of the parameters.

	Returns
	--------
	An array containing initial guesses for params.
	*/
	var initial_params = new Array(num_params);
	for (i=0; i<num_params; i++){
		var min_value = min_params[i];
		var max_value = max_params[i];
		initial_params[i] = Math.random() * (max_value - min_value) + min_value;
	}
	return initial_params;
}




// Find the next point in the markov chain.
function markov_chain(params, std_params){
	/*
	Params
	------
	params: Array containing the params.
	std_params: Array, standard deviation of the parameters.

	Returns
	-------
	Next params in the Markov CHain.
	*/
	var new_params = new Array(params.length);
	for (j=0; j<params.length; j++){
		var x = params[j];
		var x_err = std_params[j];
		new_params[j] = d3.random.normal(x, x_err)();

	}
	new_params[2] = 25.0;
	return new_params
}





// Compute the Chi-square for the params.
// For a linear fitting function.
function chi_square(data, params, fit){
	/*
	Params
	-------
	data: An object (array) of objects containing data.
	Each element if of form {'x': x, 'y': y, 'y_err': y_err}
	params: Array containing the params.
	fit: String, type of fitting function.

	Returns
	--------
	A floating number, value of chi square.
	*/
	// alert(fit);
	var chi_sq = 0.0;
	for (i=0; i<data.length; i++){
		if (fit == 'linear'){
			var y_model = params[0] * data[i].x + params[1];
		}
		else if (fit == 'quadratic'){
			var y_model = params[0] * Math.pow(data[i].x, 2) + params[1] * data[i].x + params[2];
		}
		else{
			alert("fitting function fucked up");
		}
		// var y_model = params[0] * data[i].x + params[1];
		var chi_term = (data[i].y - y_model) / (1.0 * data[i].y_err);
		// console.log([params[0], params[1], params[2], y_model]);
		chi_sq = chi_sq + Math.pow(chi_term, 2);
	}
	return chi_sq;
}



// Metropolis-Hastings algorithm.
function metropolis_hastings(old_chi2, new_chi2){
	/*

	*/
	var chi_ratio = Math.exp(old_chi2 - new_chi2);
	var random_num = Math.random();

	if (chi_ratio >= random_num){
		return true;
	}
	else{
		return false;
	}


}


// Main MCMC function. Metropolis-Hastings algorithm.
function main_chain(data, old_params, min_params, max_params, std_params){
	/*
	Params
	------
	data: An object (Array) of objects containing data.
	num_params: Integer, number of parameters.
	Default is 2.
	min_params: Array, minimum values of the parameters.
	max_params: Array, maximum values of the parameters.
	std_params: Array, standard deviation of the parameters.

	Returns
	-------
	Next accepted point of the chain.
	*/
	var old_params = [old_params.x, old_params.y];
	var old_chiSq = chi_square(data, old_params) / 2;
	var new_params = markov_chain(old_params, std_params);
	var new_chiSq = chi_square(data, new_params) / 2;

	var chi_ratio = Math.exp(old_chiSq - new_chiSq);

	var random_num = Math.random();
	var count = 0;

	if (chi_ratio >= random_num){
		return {'x': new_params[0], 'y': new_params[1]};
		// if ((min_params[0] <= new_params[0] <= max_params[0]) && (min_params[1] <= new_params[1] <= max_params[1])){
		// 	return {'x': new_params[0], 'y': new_params[1]};
		// }
		// else{
		// 	return {'x': old_params[0], 'y': old_params[1]};
		// }
		// count ++;
		// console.log(count);
	}
	else{
		return {'x': old_params[0], 'y': old_params[1]};
	}
}





