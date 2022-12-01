function onClickRecommend(){
    console.log("Button clicked")
    var title = document.getElementById("uinamebox");
    var top_n = document.getElementById("uicount");
    
    var url = "http://127.0.0.1:5000/recommend";

    $.post(url, {
        title: title.value,
        top_n: top_n.value
    },function(data, status) {
        document.getElementById("uirecommend").innerHTML =  data ;
        console.log(status);
    }
    );
}