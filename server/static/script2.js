console.log('connected');

fetch('http://127.0.0.1:5000/get_location')
	.then(function(response) {
		// The API call was successful!
		if (response.ok) {
			return response.json();
		} else {
			return Promise.reject(response);
		}
	})
	.then(function(data) {
		// This is the JSON from our response
		console.log(data);
		const location = data.location;
		var x = document.getElementById('sl');
		for (let i of location) {
			var option = document.createElement('option');
			option.value = i;
			//console.log(option.value);
			option.text = i;
			x.add(option);
		}
	})
	.catch(function(err) {
		// There was an error
		console.warn('Something went wrong.', err);
	});

document.getElementById('myform').addEventListener('submit', function(event) {
	event.preventDefault();
});

function submit2() {
	console.log('submitted');
	fetch('http://127.0.0.1:5000/get_price', {
		body: new FormData(document.getElementById('myform')),
		header: { 'Access-Control-Allow-Origin': '*' },

		method: 'post'
	})
		.then(function(response) {
			if (response.ok) {
				return response.json();
			} else {
				console.log(response);
				return Promise.reject(response);
			}
		})
		.then(function(data) {
			// This is the JSON from our response
			//console.log(data);
			document.getElementById('price').innerHTML = parseInt(data.price).toString() + ' lakhs';
		})
		.catch(function(err) {
			// There was an error
			console.warn('Something went wrong.', err);
		});
}
