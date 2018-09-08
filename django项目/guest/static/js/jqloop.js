$(function(){
	$('#ul li').eq(0).css('background-color','red');
	var currentPage = 1;
	var timer = setInterval(startLoop,2000);
	function startLoop(){
		currentPage++;
	    changePage();
	
	}
    function changePage(){
    	if(currentPage==9){
			currentPage = 1;
		}
		if(currentPage==0){
			currentPage = 8;
		}

		$('#div img').attr('src',"/static/image1/" + currentPage  + ".jpg");

		$('#ul li').each(function(){
		      $(this).css('background-color','lightgray')
		})
		var index = currentPage - 1;		
		$('#ul li').eq(index).css('background-color','red');
    }
    //鼠标监听事件
    $('#div').bind('mouseover',function(){
    	clearInterval(timer);
    	$(".btn").css('display','block');
    });	
    
    $('#div').bind('mouseout',function(){
    	//恢复定时器
    	timer = setInterval(startLoop,1000);
    	$(".btn").css('display','none');
    	changePage();
    });	
    
    //按钮移入移出事件
    $(".btn").bind('mouseover',function(){
    	this.css('background-color','rgba(0,0,0,0.6)');
    })
    $(".btn").bind('mouseout',function(){
    	this.css('background-color','rgba(0,0,0,0.2)');
    })
    
    //鼠标点击按钮事件
    $(".left_btn").bind('click',function(){
    	currentPage--;
    	changePage();
    })
    $(".right_btn").bind('click',function(){
    	currentPage++;
    	changePage();
    })
    
    //鼠标移入小圆点
    $('#ul li').each(function(index){
    	$(this).bind('mouseover',function(){
    		currentPage = index+1;
    	    changePage();
    	})
    })
    
})
