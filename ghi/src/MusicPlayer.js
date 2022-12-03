const MusicPlayer = (spotifyUrl) => {
	const artistId = spotifyUrl["spotifyUrl"].split("/").pop();
	console.log(artistId);
	return (
		<iframe
			style={{ borderRadius: 12 }}
			src={`https://open.spotify.com/embed/artist/${artistId}?utm_source=generator`}
			width="100%"
			height="380"
			frameBorder="0"
			allowFullScreen=""
			title={{ artistId }}
			allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
			loading="lazy"></iframe>
	);
};

export default MusicPlayer;
