const MusicPlayer = (spotifyUrl) => {
	const artistId = spotifyUrl["spotifyUrl"].split("/").pop();
	return (
		<iframe
			style={{ borderRadius: 12 }}
			src={`https://open.spotify.com/embed/artist/${artistId}?utm_source=oembed`}
			width="100%"
			height="380"
			frameBorder="0"
			allowFullScreen=""
			title="Artist IFRAME"
			allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
			loading="lazy"></iframe>
	);
};

export default MusicPlayer;
