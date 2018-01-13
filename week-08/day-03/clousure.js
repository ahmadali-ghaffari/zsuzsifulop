'use strict'

var sellProduct = function() {
	var cash = 0;
	return function(price) {
	    cash += price;
	    console.log(cash);
        
	}
}

var sell = sellProduct();
sell(50);
sell(50);