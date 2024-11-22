# Interactive-IPL-Player-Auction-Simulation
A dynamic web-based platform for conducting IPL-style player auctions, featuring real-time bid animations, speech synthesis, team selection, and role-based player bidding. Built with Flask, HTML/CSS, JavaScript, and custom animations.

## Features  

- **Player Auction Simulation**: Conduct IPL-style player auctions with dynamic bid updates.  
- **Real-Time Speech Synthesis**: Announces the bids and player statuses (sold/unsold) with a realistic auctioneer voice.  
- **Team Selection**: Choose from IPL teams, complete with their logos and a visual selector.  
- **Dynamic Bid Animations**: Digit-specific animations and smooth transitions for bids.  
- **Custom Base Price Handling**: Automatically starts bidding from a player's base price.  
- **Responsive UI**: Designed for seamless user interaction across devices.  

## Tech Stack  

- **Backend**: [Flask](https://flask.palletsprojects.com/)  
- **Frontend**: HTML, CSS (Digital-7 font for auction display), JavaScript  
- **Voice Integration**: Web Speech API  

## Installation

1.install dependencies:
pip install flask numpy

2.Start the Flask server:
python app.py

3.Open your browser and navigate to http://127.0.0.1:5000

## Usage
- Select a Player: Players appear for auction one at a time.
- Place Bids: Use the "Increase Bid" button to place bids. The bidding will start from the base price and increase dynamically based on the rules:
  - Below ₹2 Cr: Increases by ₹0.1 Cr
  - ₹2 Cr and above: Increases by ₹0.2 Cr
- Team Selection: Choose a team to buy the player or mark them as unsold.
- Experience the Auctioneer: Bids and results are announced in real-time using the Web Speech API.

## Acknowledgements
- Digital-7 Font for the auction-style display.
- IPL and team logos are used for simulation purposes only.

## Future Enhancements
- Add player stats and details.
- Implement real-time multi-user bidding using WebSockets.
- Enhance responsiveness and add a mobile-friendly UI.

