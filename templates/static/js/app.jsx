import React from "react";
import StyleSheet from "react-style";

require('../css/mainPage.css');

const styles = StyleSheet.create({
  main: {
    color: 'green'
  },
});


export default class App extends React.Component{
  render() {

    return (
      <div>
      <div><h1>Emma Bareis</h1>
      <h2>Software Engineer</h2></div>
      <div styles={[styles.main]}>Hello!  My name is Emma Bareis and I am a software developer from Dallas, Tx with experience developing for the market research and health insurance industries.  I have been involved in development professionally since 2014 and have been experimenting and tinkering on my own time for longer.  My most recent experience lies with C#, Azure, react, and knockout.  In my own time I enjoy experimenting with Python and C, and have even delved into a specific implementation of Z80 assembly for the Nintendo game boy.  When not working, my hobbies include collecting and playing retro video games, playing roller derby, and experimenting with game boy software development.</div>
      </div>
    );
  }
}
