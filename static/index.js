window.addEventListener('scroll', () => {
    localStorage.setItem('scrollY',window.scrollY);
}, false);

window.addEventListener('keyup', () => {
    if (document.getElementById('music-link-input').value.includes('.spotify')) {
        showTags()
    } else {
        hideTags()
    }
});

window.addEventListener('load', () => {
    const y = localStorage.getItem('scrollY');
    if (y) {
        document.documentElement.scrollTop = y;
    };
}, false);

// Toggle open/close form
const openForm = () => {
    document.getElementById(`add-container`).style.display = 'flex';
}

const closeForm = () => {
    document.getElementById(`add-container`).style.display = 'none';
}

// Toggle username field
const hideUsername = () => {
    document.getElementById('user').style.display = 'none';
}
const showUsername = () => {
    document.getElementById('user').style.display = 'block';
}

// Toggle tags field
const hideTags = () => {
    document.getElementById('body-tags').style.display = 'none';
}
const showTags = () => {
    document.getElementById('body-tags').style.display = 'block';
}

// Toggle between which form content to show
const showFormBody = (type) => {
    const showForm = document.getElementById('body-shows');
    const musicForm = document.getElementById('body-music');

    switch (type) {
        case 'shows':
            showForm.style.display = 'block';
            musicForm.style.display = 'none';
            showTags()
            break;
        case 'music':
            showForm.style.display = 'none';
            musicForm.style.display = 'block';
            break;
        default:
            break;
    }
}

// Send new post to the backend
const addPost = async () => {
    // Determine the type post being added 
    const type = document.getElementById('shows-radio').checked ? 'shows' : 'music';
    const username = document.getElementById('username-input').value;
    const tags = document.getElementById('tag-input').value;

    if (type === 'shows') {
        await addShow(username, tags);
    } else if (type === 'music') {
        await addMusic(username, tags);
    };

    closeForm();
}

const addShow = async (username, tags) => {
    const title = document.getElementById('title-input').value;
    const link = document.getElementById('show-link-input').value;
    const body = { username, title, link, tags};
    
    // Send request
    try {
        const res = await fetch('/api/shows', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', },
            body: JSON.stringify(body),
        });
        // TODO: Add it in as a new item
    } catch (err) {
        console.log(err);
    }
};

const addMusic = async (username, tags) => {
    const link = document.getElementById('music-link-input').value;
    const body = { username, link, tags};
    
    // Send request
    try {
        const res = await fetch('/api/music', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', },
            body: JSON.stringify(body),
        });
        // TODO: Add it in as a new item
    } catch (err) {
        console.log(err);
    }
};

// Create DOM element for posts clicked on
const savePost = (post) => {
    const container = document.getElementById('saved-posts');
    
    const firstChild = container.firstElementChild;
    
    // If this is the first post, get rid of the filler text
    if (firstChild.tagName === 'P') {
        firstChild.remove();
    }

    // Create the new post
    const newPost = document.createElement('DIV');
    newPost.classList.add('post');
    newPost.classList.add('saved');
    
    const username = document.createElement('P');
    username.classList.add('post-uploader');
    username.innerText = post.username;

    const imageContainer = document.createElement('DIV');
    imageContainer.classList.add('image-gradient');
    
    const image = document.createElement('IMG');
    image.setAttribute('src', post.link);
    
    imageContainer.appendChild(image);
    newPost.appendChild(username);
    newPost.appendChild(imageContainer);

    // Add to list of saved posts
    container.appendChild(newPost);
}
