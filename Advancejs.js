//let + const
const player = "bobby";
let experience = 100;
let wizardLevel = true;

if (experience < 110) {
	let wizardLevel = false;
	console.log("inside",wizardLevel);
}
console.log("outside",wizardLevel);

const a = {
	name:"Karan",
	age :"19"
}

// Destructuring

const marvel = {
	hero:"ironman",
	movies:"Ironman1,Ironman2,Ironman3",
	name:"Robert Downey Jr."
}   

const {hero,name} = marvel;
let {movies}= marvel;

//Object properties

const name = "The Nun";
const a = {
	[name]:"movie",
	[1 + 2]:"part"
}

const name="Karan";
const age="19";
const gender="Male";

const details={
	name,
	age,
	gender
}

//Template Strings
const name = "Ted";
const age = 34;
const pet = "cockmouse";

const greetings = `Hello ${name} .You are ${age} .And you have nice ${pet}`;

//Symbols
//It always get these completely  unique types.So there never going to be any conflict . 
let sym1=Symbol();
let sym2=Symbol("sym2");
let sym3=Symbol("sym2");

sym2 === sym3

// Arrow function
function add1(a,b) {
	return a + b;
}

const add2 = (a,b) => a*b;  //Arrow function statement

//Clousers - a function ran. The function executed. it's never going to execute again.
//But it's going to remember that there are refrences to those variables
//So the child scope has always access to the parent scope.

const first = () =>{
	const greet = "Hi!";
	const second = () => {
		alert(greet);
	}
	return second;
}

const newFunc = first();
newFunc();

//Currying
const multiply = (a,b) => a*b;
const curriedMultiply = (a) => (b) => a*b;
const multiplyBY5 = curriedMultiply(5);

//Compose
const compose = (a,b) => (num) => a(b(num));
const sum = (num1) => num1 + 1;
compose(sum,sum)(10);