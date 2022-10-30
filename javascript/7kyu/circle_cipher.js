function encode (st){
	s = st.split('');
	news = '';
	while (s.length){
		switch (s.length){
			case 1:
				news += s.shift();
				return news;
			default:
				news += s.shift() + s.pop();
				break;
		}
	}
	return news;
}

function decode (s){
	var odd = [], even = [];
	for(var i = 1; i <= s.length; i++){
		if(i % 2 == 0){
			even.push(i);
		}else{
			odd.push(i);
		}
	}
	var w = '';
	for(var x of odd){
		w += s[x-1];
	}
	while(even.length){
		w += s[even.pop()-1];
	}
	return w;
}
console.log(encode('codewars'));
console.log(encode('white'));
console.log();
console.log(decode(encode('codewars')));
console.log(decode(encode('white')));
