#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
	print() {
		let a;
		let b;
		let holder = '';
		for (a = 0; a < this.width; a++) {
			if (a > 0){
				holder = '\n'
			}
			for (b = 0; b < this.height; b++) {
				holder += 'X';
			}
				
		}
		console.log (holder);
	}
}
module.exports = Rectangle;
