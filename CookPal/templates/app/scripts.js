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



 
  // Get all the reply buttons
  document.querySelectorAll('.replybtn').forEach(button => {
    button.addEventListener('click', function() {
      // Get the ID of the reply form to be displayed
      const replyFormId = this.getAttribute('data-comment-id');
      // Display the corresponding reply form
      document.getElementById(replyFormId).style.display = 'block';
    });
  });

  // Get all the submit reply buttons
  document.querySelectorAll('.submit-reply').forEach(button => {
    button.addEventListener('click', function() {
      // Add logic here to submit a reply, like using AJAX to send a reply to the server
      alert('Reply submitted (this should be replaced with the actual submission logic here)');
      // Hide the reply form
      this.parentElement.style.display = 'none';
    });
  });


  