var sum = {
    sumElements: function(listOfNumber){
        if (Array.isArray(listOfNumber) === false){
            throw new Error ('"listOfNumber" is not an array')
        } else {
            var currentSum = 0;
            listOfNumber.forEach(function(element) {
                currentSum += element
        });
        return currentSum;
    };
    }
}
module.exports = sum;
try {
	sum.sumElements([11,1]);
} catch (err) {
	console.log('catching error:');
	console.log(err.message);
}


