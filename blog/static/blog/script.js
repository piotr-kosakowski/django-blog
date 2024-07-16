// script.js

document.addEventListener("DOMContentLoaded", function () {
    var pageName = '{{ page_name }}';
    var mainElement = document.querySelector('main');

    if (pageName === 'index') {
        mainElement.style.justifyContent = 'space-between';

    } else if (pageName === 'all_posts') {
        mainElement.style.flexDirection = 'column';
    } else {
        mainElement.style.justifyContent = 'center';
    }
    var postsDiv = document.querySelector('#posts-div');
    if(postsDiv) {
        //select height of posts-div
        var postsDivHeight = postsDiv.clientHeight;
        // set discussion-div height to posts-div height
        var discussionDiv = document.querySelector('#discussion-div');
        discussionDiv.style.height = `${postsDivHeight }px`;

    }

    var postElement = document.querySelector('.extends-base');
    if (!postElement) {
        return;
    }
    var postId = postElement.getAttribute('data-post-id');
    var likeButton = document.querySelector(`#like-button-${postId}`);
    var userId = postElement.getAttribute('data-user-id');
    fetch(`/blog/check_like_post/${postId}/`)
        .then(response => {
            // Check if the response status is in the success range
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            var userHasLiked = data.likes.includes( Number(userId));
            likeButton.innerText = userHasLiked ? 'Unlike' : 'Like';})

        .catch(error => console.error('Error:', error));

});

async function likePost(postId) {
    fetch(`/blog/like_post/${postId}/`)
        .then(response => {
            // Check if the response status is in the success range
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {

            const likesElement = document.querySelector(`#likes-${postId}`);
            likesElement.innerText = `Likes: ${data.likes_count}`;
            const likeButton = document.querySelector(`#like-button-${postId}`);

            const userHasLiked = data.likes.includes(data.currentUserId);

            // Update the button text
            likeButton.innerText = userHasLiked ? 'Unlike' : 'Like';})
        .catch(error => console.error('Error:', error));
}



