// 模态框功能：点击证明按钮显示大图或PDF
var modal = document.getElementById("modal");
var modalImg = document.getElementById("modal-img");
var span = document.getElementsByClassName("close")[0];

document.querySelectorAll('.proof-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        var src = this.getAttribute('data-src');
        // 如果是PDF，我们暂时用浏览器打开新标签页（更简单）
        if (src.endsWith('.pdf')) {
            window.open(src, '_blank');
        } else {
            modal.style.display = "block";
            modalImg.src = src;
        }
    });
});

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}