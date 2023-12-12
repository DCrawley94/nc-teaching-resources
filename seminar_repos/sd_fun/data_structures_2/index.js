function createPlaylist() {}

module.exports = createPlaylist;

/*
You are starting up your own music streaming service to rival Spotify.

Your task is to write a createPlaylist factory function that produces playlist objects for your users to listen to.
Your users should: 
  - be able to name their playlists
  - add tracks to it by name
  - get the name of the current track
  - move on to the next track in the list.


const partyAnthems = createPlaylist('absolute bangers');

partyAnthems.name; // 'absolute bangers'

partyAnthems.addTrack('superstition');
partyAnthems.addTrack('uptown girl');
partyAnthems.tracks; // ['superstition', 'uptown girl']

partyAnthems.getCurrentTrack(); // `Now playing: superstition`

partyAnthems.nextTrack();
partyAnthems.getCurrentTrack(); // 'uptown girl'
*/
