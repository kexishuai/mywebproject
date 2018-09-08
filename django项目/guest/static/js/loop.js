//1.获取所有的标签对象
var jsBox = document.getElementById("box");
var jsPic = document.getElementById("pic");
var jsLeft = document.getElementById("leftbt");
var jsRight = document.getElementById("rightbt");
var jsLiArr = document.getElementsByTagName("li");

//2.初始状态下，将第一个li设置为选中状态，红色
jsLiArr[0].style.backgroundColor = "red";

//3.启动一个间歇性定时器：每隔一段时间切换图片
//定义一个变量，用于记录是第几张图片
var currentPage = 1;
var timer = setInterval(startLoop,1000);
function startLoop(){
	//可以显示不同的图片，按照顺序显示的
	currentPage++;
	
	changePage();
}

function changePage(){
	//临界条件的判断
	//当图片显示到最后一张的时候，重新从第一张开始显示
	if(currentPage == 9){
		currentPage = 1;
	}
	//当图片显示第一张的时候，如果再次倒退，则重新显示到最后一张
	if(currentPage == 0){
		currentPage = 8;
	}
	
	//给img标签赋值
	jsPic.src = "image1/" + currentPage  + ".jpg";
	
	//重新设置小圆点的选中状态
	//清除原有的选中状态
	for(var i = 0; i < jsLiArr.length;i++) {
		jsLiArr[i].style.backgroundColor = "lightgray";
	}
	//设置当前选中的小圆点
	jsLiArr[currentPage - 1].style.backgroundColor = "red";
}

//3.div的事件处理
//思路：当鼠标移动到div的上面，则此时定时器停止工作，左右按钮显示出来；
//当鼠标移出div的时候，定时器回复工作，左右按钮隐藏
//鼠标移入
jsBox.addEventListener("mouseover",overFunc,false);
function overFunc(){
	//停止定时器
	clearInterval(timer);
	//左右按钮显示出来
	jsLeft.style.display = "block";
	jsRight.style.display = "block";
}

//鼠标移出
jsBox.addEventListener("mouseout",outFunc,false);
function outFunc(){
	//恢复定时器
	timer = setInterval(startLoop,1000);
	//左右按钮隐藏
	jsLeft.style.display = "none";
	jsRight.style.display = "none";
}

//4.左右按钮的事件处理
//思路：当鼠标进入左右按钮的时候，左右按钮对应的div颜色加深；当鼠标移出左右按钮的div的时候，颜色恢复
//鼠标进入左右按钮
jsLeft.addEventListener("mouseover",deep,false);
jsRight.addEventListener("mouseover",deep,false);
function deep(){
	this.style.backgroundColor = "rgba(0,0,0,0.6)";
}

//鼠标移出左右按钮
jsLeft.addEventListener("mouseout",nodeep,false);
jsRight.addEventListener("mouseout",nodeep,false);
function nodeep(){
	this.style.backgroundColor = "rgba(0,0,0,0.2)";
}

//5.当点击左右按钮的时候
jsLeft.addEventListener("click",function(){
	currentPage--;
	changePage();
	
},false);
jsRight.addEventListener("click",function(){
	currentPage++;
	changePage();
},false);

//6.鼠标移入小圆点
//思路:mouseover.当鼠标移入到小圆点的时候，直接切换指定的图片
for(var i = 0; i< jsLiArr.length;i++) {
	//给每个小圆点做一个标记，用于记录当前是第几张图片
	jsLiArr[i].index = i + 1;
	
	//监听每个小圆点
	jsLiArr[i].addEventListener("mouseover",function(){
		currentPage = parseInt(this.index);
		changePage();
	},false);
}
