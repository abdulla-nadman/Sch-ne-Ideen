function share(platform) {
    let url = encodeURIComponent(window.location.href);
    let shareUrl = '';
    if (platform === 'facebook') {
        shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
    } else if (platform === 'twitter') {
        shareUrl = `https://twitter.com/intent/tweet?url=${url}`;
    } else if (platform === 'linkedin') {
        shareUrl = `https://www.linkedin.com/shareArticle?url=${url}`;
    }
    window.open(shareUrl, '_blank');
}