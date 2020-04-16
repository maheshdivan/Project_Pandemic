var canvas = document.getElementById('c');
var ctx = canvas.getContext('2d');
var H = window.innerHeight;
var W = window.innerWidth;
canvas.height = H;
canvas.width = W;

var NBR_PARTICLES = 300;
var INTENSITY = 55;
var BLUE_RATIO = 5;

particles = [];
for (var i = 0; i < NBR_PARTICLES; i++) {
	particles.push( new particle(i) );
};

function particle(i){
	this.size = rand(0, 1.4);
	this.x = W / 2;
	this.y = H / 2;
	this.vx = rand(-2, 2);
	this.vy = rand(-2, 2);
	this.decay = rand(0.5, 1);
	this.c = 0;
}

function draw(){
	for (var i = 0; i < NBR_PARTICLES; i++) {
		p = particles[i];
		ctx.fillStyle = color(p.size);
		ctx.beginPath();
		ctx.arc(p.x, p.y, p.size, Math.PI*2, false);
		ctx.fill();
		p.size *= p.decay;
		p.x += p.vx;
		p.y += p.vy;
		p.vx += rand(-.2, .2);
		p.vy += rand(-.2, .2);
		p.c++;
		if(p.size < .2){
			particles[i] = new particle(i);
		}
	};
}

function color(i){
	value = 255 - Math.round( (i * (255 / NBR_PARTICLES)) * INTENSITY);
	return "rgba(" + value + ", 0, " + Math.round((NBR_PARTICLES - i) / BLUE_RATIO) + ", .75)";
}


setInterval(draw, 2);


/*************************
	CONSTRUCT FUNCTIONS
**************************/

function rand(min, max){
	value = min + Math.random() * ( max - min );
	return value;
}
function cd(args){ // FOR DEBUG
	console.dir(args);
}