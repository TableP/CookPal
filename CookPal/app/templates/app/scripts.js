document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.star');
    stars.forEach(function(star) {
      star.addEventListener('mouseover', starOver);
      star.addEventListener('click', starClick);
    });
  
    function starOver(e) {
      const value = +e.target.dataset.value;
      stars.forEach(function(star) {
        if (+star.dataset.value <= value) {
          star.textContent = '★'; 
        } else {
          star.textContent = '☆'; 
        }
      });
    }
  
    function starClick(e) {
      const value = +e.target.dataset.value;
      console.log(`Rated: ${value} stars`);
    }
  });



 
  // 获取所有的回复按钮
  document.querySelectorAll('.replybtn').forEach(button => {
    button.addEventListener('click', function() {
      // 获取要显示的回复表单的ID
      const replyFormId = this.getAttribute('data-comment-id');
      // 显示对应的回复表单
      document.getElementById(replyFormId).style.display = 'block';
    });
  });

  // 获取所有的提交回复按钮
  document.querySelectorAll('.submit-reply').forEach(button => {
    button.addEventListener('click', function() {
      // 这里可以添加提交回复的逻辑，例如使用AJAX发送回复内容到服务器
      alert('回复已提交（这里应该替换为实际的提交逻辑）。');
      // 隐藏回复表单
      this.parentElement.style.display = 'none';
    });
  });


  