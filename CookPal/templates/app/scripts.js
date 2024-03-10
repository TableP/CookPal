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




  // get all reply button
  document.querySelectorAll('.replybtn').forEach(button => {
    button.addEventListener('click', function() {
      // get id for reply form
      const replyFormId = this.getAttribute('data-comment-id');
      // show the reply form
      document.getElementById(replyFormId).style.display = 'block';
    });
  });

  // get all submit reply button
  document.querySelectorAll('.submit-reply').forEach(button => {
    button.addEventListener('click', function() {
      // use AJAX to send reply to server
      alert('Reply Submitted!');
      // hide reply form
      this.parentElement.style.display = 'none';
    });
  });


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
