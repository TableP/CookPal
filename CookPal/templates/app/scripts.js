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



 
<<<<<<< HEAD:CookPal/templates/app/scripts.js
  // Get all the reply buttons
  document.querySelectorAll('.replybtn').forEach(button => {
    button.addEventListener('click', function() {
      // Get the ID of the reply form to be displayed
      const replyFormId = this.getAttribute('data-comment-id');
      // Display the corresponding reply form
=======
  // get all reply button
  document.querySelectorAll('.replybtn').forEach(button => {
    button.addEventListener('click', function() {
      // get id for reply form
      const replyFormId = this.getAttribute('data-comment-id');
      // show the reply form
>>>>>>> origin/front-end:CookPal/app/templates/app/scripts.js
      document.getElementById(replyFormId).style.display = 'block';
    });
  });

<<<<<<< HEAD:CookPal/templates/app/scripts.js
  // Get all the submit reply buttons
  document.querySelectorAll('.submit-reply').forEach(button => {
    button.addEventListener('click', function() {
      // Add logic here to submit a reply, like using AJAX to send a reply to the server
      alert('Reply submitted (this should be replaced with the actual submission logic here)');
      // Hide the reply form
=======
  // get all submit reply button
  document.querySelectorAll('.submit-reply').forEach(button => {
    button.addEventListener('click', function() {
      // use AJAX to send reply to server
      alert('Reply Submitted!');
      // hide reply form
>>>>>>> origin/front-end:CookPal/app/templates/app/scripts.js
      this.parentElement.style.display = 'none';
    });
  });


<<<<<<< HEAD:CookPal/templates/app/scripts.js
  
=======
  function copyLink() {
    var copyText = document.getElementById("shareLinkInput");
    copyText.select(); // select text
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value); // copy the text to clipboard
  
    navigator.clipboard.writeText(copyText.value).then(() => {
      // show Toast after copied
      var toastEl = document.getElementById('copyToast');
      var toast = new bootstrap.Toast(toastEl);
      toast.show();
      var shareModalEl = document.getElementById('shareModal');
      var shareModal = bootstrap.Modal.getInstance(shareModalEl);
      shareModal.hide();
    }, () => {
      // fail to copy
      // I don't think we need this
    });
  }
>>>>>>> origin/front-end:CookPal/app/templates/app/scripts.js
