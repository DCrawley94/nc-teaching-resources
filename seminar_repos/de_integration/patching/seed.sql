DROP DATABASE IF EXISTS nc_games;
CREATE DATABASE nc_games;

\c nc_games

DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS games;

CREATE TABLE games (
  game_id SERIAL PRIMARY KEY,  
  game_title VARCHAR NOT NULL,
  release_year INT,
  console_name VARCHAR NOT NULL,
  image_url VARCHAR
);

CREATE TABLE reviews (
  review_id SERIAL PRIMARY KEY,
  game_id INT NOT NULL REFERENCES games(game_id),
  username VARCHAR NOT NULL,
  comment VARCHAR NOT NULL,
  rating INT
);

INSERT INTO games
(game_title, release_year, console_name, image_url)
VALUES 
('Mario Kart 64', 1996, 'N64', 'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg'),
('Donkey Kong', 1983, 'NES', 'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nes/nes_donkeykong_thumb.jpg'),
('Mario Bros', 1985, 'NES', 'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nes/nes_mariobros_thumb.jpg');

INSERT INTO reviews
(username, game_id, comment, rating)
VALUES
('fola',1,'Cupcake ipsum dolor sit amet jelly gingerbread. Cookie apple pie tiramisu lollipop jujubes candy canes cheesecake I love macaroon. Bear claw jelly-o sugar plum jelly beans. Sweet roll sweet roll topping. Marzipan chocolate sesame snaps icing carrot cake cotton candy soufflé I love. Topping ice cream cotton candy macaroon I love brownie. Pudding I love icing caramels donut ice cream chocolate cake marzipan sesame snaps. I love I love powder jelly beans. Cookie gummies cotton candy candy sugar plum chocolate cake jelly beans gummi bears sweet roll. Lemon drops cake caramels liquorice cotton candy apple pie cupcake jujubes. Halvah carrot cake pie candy I love I love I love apple pie sweet roll. Pie pudding chupa chups jelly brownie powder sweet roll. I love donut gingerbread brownie candy canes I love I love powder.',5),
('rogersop',2,'Skate ipsum dolor sit amet, alley oop vert mute-air Colby Carter flail 180 berm. Half-cab camel back ollie transition ledge Wes Humpston 1080. Carve casper switch kickturn late downhill. Hardware nosebone Rick McCrank bluntslide bigspin steps egg plant. Slap maxwell roll-in airwalk fast plant fastplant pivot.',4),    
('izzi',3,'Zombies reversus ab inferno, nam malum cerebro. De carne animata corpora quaeritis. Summus sit​​, morbo vel maleficia? De Apocalypsi undead dictum mauris. Hi mortuis soulless creaturas, imo monstra adventus vultus comedat cerebella viventium. Qui offenderit rapto, terribilem incessu. The voodoo sacerdos suscitat mortuos comedere carnem. Search for solum oculi eorum defunctis cerebro. Nescio an Undead zombies. Sicut malus movie horror.',5),    
('fola',3,'Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. The concept of Lorem Ipsum was created by and for the Chinese in order to make U.S. design jobs non-competitive. Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. You know, it really doesn’t matter what you write as long as you’ve got a young, and beautiful, piece of text.',5),    
('nom',2,'Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. The concept of Lorem Ipsum was created by and for the Chinese in order to make U.S. design jobs non-competitive. Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. You know, it really doesn’t matter what you write as long as you’ve got a young, and beautiful, piece of text.',5),    
('shd',3,'Vexillologist try-hard narwhal plaid polaroid celiac yuccie. Small batch tote bag pug kombucha laborum taxidermy intelligentsia crucifix vinyl literally tumblr poke bushwick readymade. Tacos sustainable nostrud humblebrag fam. Coloring book et deep v chillwave cornhole pitchfork air plant master cleanse fingerstache prism gluten-free laborum beard hammock. Affogato brooklyn cornhole salvia. Leggings slow-carb roof party fingerstache. Live-edge tempor thundercats truffaut lomo, cred shaman.',4),    
('shd',3,'Vexillologist try-hard narwhal plaid polaroid celiac yuccie. Small batch tote bag pug kombucha laborum taxidermy intelligentsia crucifix vinyl literally tumblr poke bushwick readymade. Tacos sustainable nostrud humblebrag fam. Coloring book et deep v chillwave cornhole pitchfork air plant master cleanse fingerstache prism gluten-free laborum beard hammock. Affogato brooklyn cornhole salvia. Leggings slow-carb roof party fingerstache. Live-edge tempor thundercats truffaut lomo, cred shaman.',5),    
('acox', 1, 'Zombies reversus ab inferno, nam malum cerebro. De carne animata corpora quaeritis. Summus sit​​, morbo vel maleficia? De Apocalypsi undead dictum mauris. Hi mortuis soulless creaturas, imo monstra adventus vultus comedat cerebella viventium. Qui offenderit rapto, terribilem incessu. The voodoo sacerdos suscitat mortuos comedere carnem. Search for solum oculi eorum defunctis cerebro. Nescio an Undead zombies. Sicut malus movie horror.',5),    
('antmed',2,'Vexillologist try-hard narwhal plaid polaroid celiac yuccie. Small batch tote bag pug kombucha laborum taxidermy intelligentsia crucifix vinyl literally tumblr poke bushwick readymade. Tacos sustainable nostrud humblebrag fam. Coloring book et deep v chillwave cornhole pitchfork air plant master cleanse fingerstache prism gluten-free laborum beard hammock. Affogato brooklyn cornhole salvia. Leggings slow-carb roof party fingerstache. Live-edge tempor thundercats truffaut lomo, cred shaman.',2),    
('izzi',2,'Zombies reversus ab inferno, nam malum cerebro. De carne animata corpora quaeritis. Summus sit​​, morbo vel maleficia? De Apocalypsi undead dictum mauris. Hi mortuis soulless creaturas, imo monstra adventus vultus comedat cerebella viventium. Qui offenderit rapto, terribilem incessu. The voodoo sacerdos suscitat mortuos comedere carnem. Search for solum oculi eorum defunctis cerebro. Nescio an Undead zombies. Sicut malus movie horror.',1),    
('izzi',2,'Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. The concept of Lorem Ipsum was created by and for the Chinese in order to make U.S. design jobs non-competitive. Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. You know, it really doesn’t matter what you write as long as you’ve got a young, and beautiful, piece of text.',5),    
('dedekind',2,'Zombies reversus ab inferno, nam malum cerebro. De carne animata corpora quaeritis. Summus sit​​, morbo vel maleficia? De Apocalypsi undead dictum mauris. Hi mortuis soulless creaturas, imo monstra adventus vultus comedat cerebella viventium. Qui offenderit rapto, terribilem incessu. The voodoo sacerdos suscitat mortuos comedere carnem. Search for solum oculi eorum defunctis cerebro. Nescio an Undead zombies. Sicut malus movie horror.',4),    
('antmed',3,'Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. The concept of Lorem Ipsum was created by and for the Chinese in order to make U.S. design jobs non-competitive. Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. You know, it really doesn’t matter what you write as long as you’ve got a young, and beautiful, piece of text.',5),    
('nom',3,'Cupcake ipsum dolor sit amet jelly gingerbread. Cookie apple pie tiramisu lollipop jujubes candy canes cheesecake I love macaroon. Bear claw jelly-o sugar plum jelly beans. Sweet roll sweet roll topping. Marzipan chocolate sesame snaps icing carrot cake cotton candy soufflé I love. Topping ice cream cotton candy macaroon I love brownie. Pudding I love icing caramels donut ice cream chocolate cake marzipan sesame snaps. I love I love powder jelly beans. Cookie gummies cotton candy candy sugar plum chocolate cake jelly beans gummi bears sweet roll. Lemon drops cake caramels liquorice cotton candy apple pie cupcake jujubes. Halvah carrot cake pie candy I love I love I love apple pie sweet roll. Pie pudding chupa chups jelly brownie powder sweet roll. I love donut gingerbread brownie candy canes I love I love powder.',3),    
('anatd',2,'Zombies reversus ab inferno, nam malum cerebro. De carne animata corpora quaeritis. Summus sit​​, morbo vel maleficia? De Apocalypsi undead dictum mauris. Hi mortuis soulless creaturas, imo monstra adventus vultus comedat cerebella viventium. Qui offenderit rapto, terribilem incessu. The voodoo sacerdos suscitat mortuos comedere carnem. Search for solum oculi eorum defunctis cerebro. Nescio an Undead zombies. Sicut malus movie horror.',5),    
('izzi',3,'Vexillologist try-hard narwhal plaid polaroid celiac yuccie. Small batch tote bag pug kombucha laborum taxidermy intelligentsia crucifix vinyl literally tumblr poke bushwick readymade. Tacos sustainable nostrud humblebrag fam. Coloring book et deep v chillwave cornhole pitchfork air plant master cleanse fingerstache prism gluten-free laborum beard hammock. Affogato brooklyn cornhole salvia. Leggings slow-carb roof party fingerstache. Live-edge tempor thundercats truffaut lomo, cred shaman.',5),    
('rogersop', 1,'Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. The concept of Lorem Ipsum was created by and for the Chinese in order to make U.S. design jobs non-competitive. Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. You know, it really doesn’t matter what you write as long as you’ve got a young, and beautiful, piece of text.',5),    
('acox',3,'Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. The concept of Lorem Ipsum was created by and for the Chinese in order to make U.S. design jobs non-competitive. Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. You know, it really doesn’t matter what you write as long as you’ve got a young, and beautiful, piece of text.',5),    
('acox',3,'Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. The concept of Lorem Ipsum was created by and for the Chinese in order to make U.S. design jobs non-competitive. Lorem Ipsum is the single greatest threat. We are not - we are not keeping up with other websites. You know, it really doesn’t matter what you write as long as you’ve got a young, and beautiful, piece of text.',5),    
('anatd',2,'Skate ipsum dolor sit amet, alley oop vert mute-air Colby Carter flail 180 berm. Half-cab camel back ollie transition ledge Wes Humpston 1080. Carve casper switch kickturn late downhill. Hardware nosebone Rick McCrank bluntslide bigspin steps egg plant. Slap maxwell roll-in airwalk fast plant fastplant pivot.',5),    
('nom',2,'Zombies reversus ab inferno, nam malum cerebro. De carne animata corpora quaeritis. Summus sit​​, morbo vel maleficia? De Apocalypsi undead dictum mauris. Hi mortuis soulless creaturas, imo monstra adventus vultus comedat cerebella viventium. Qui offenderit rapto, terribilem incessu. The voodoo sacerdos suscitat mortuos comedere carnem. Search for solum oculi eorum defunctis cerebro. Nescio an Undead zombies. Sicut malus movie horror.',5),    
('anatd',2,'Vexillologist try-hard narwhal plaid polaroid celiac yuccie. Small batch tote bag pug kombucha laborum taxidermy intelligentsia crucifix vinyl literally tumblr poke bushwick readymade. Tacos sustainable nostrud humblebrag fam. Coloring book et deep v chillwave cornhole pitchfork air plant master cleanse fingerstache prism gluten-free laborum beard hammock. Affogato brooklyn cornhole salvia. Leggings slow-carb roof party fingerstache. Live-edge tempor thundercats truffaut lomo, cred shaman.',5),    
('fola',2,'Cupcake ipsum dolor sit amet jelly gingerbread. Cookie apple pie tiramisu lollipop jujubes candy canes cheesecake I love macaroon. Bear claw jelly-o sugar plum jelly beans. Sweet roll sweet roll topping. Marzipan chocolate sesame snaps icing carrot cake cotton candy soufflé I love. Topping ice cream cotton candy macaroon I love brownie. Pudding I love icing caramels donut ice cream chocolate cake marzipan sesame snaps. I love I love powder jelly beans. Cookie gummies cotton candy candy sugar plum chocolate cake jelly beans gummi bears sweet roll. Lemon drops cake caramels liquorice cotton candy apple pie cupcake jujubes. Halvah carrot cake pie candy I love I love I love apple pie sweet roll. Pie pudding chupa chups jelly brownie powder sweet roll. I love donut gingerbread brownie candy canes I love I love powder.',2),    
('fola',2,'Skate ipsum dolor sit amet, alley oop vert mute-air Colby Carter flail 180 berm. Half-cab camel back ollie transition ledge Wes Humpston 1080. Carve casper switch kickturn late downhill. Hardware nosebone Rick McCrank bluntslide bigspin steps egg plant. Slap maxwell roll-in airwalk fast plant fastplant pivot.',5),    
('anatd',3,'Vexillologist try-hard narwhal plaid polaroid celiac yuccie. Small batch tote bag pug kombucha laborum taxidermy intelligentsia crucifix vinyl literally tumblr poke bushwick readymade. Tacos sustainable nostrud humblebrag fam. Coloring book et deep v chillwave cornhole pitchfork air plant master cleanse fingerstache prism gluten-free laborum beard hammock. Affogato brooklyn cornhole salvia. Leggings slow-carb roof party fingerstache. Live-edge tempor thundercats truffaut lomo, cred shaman.',5),    
('acox',3,'Vexillologist try-hard narwhal plaid polaroid celiac yuccie. Small batch tote bag pug kombucha laborum taxidermy intelligentsia crucifix vinyl literally tumblr poke bushwick readymade. Tacos sustainable nostrud humblebrag fam. Coloring book et deep v chillwave cornhole pitchfork air plant master cleanse fingerstache prism gluten-free laborum beard hammock. Affogato brooklyn cornhole salvia. Leggings slow-carb roof party fingerstache. Live-edge tempor thundercats truffaut lomo, cred shaman.',5),    
('acox',3,'Vexillologist try-hard narwhal plaid polaroid celiac yuccie. Small batch tote bag pug kombucha laborum taxidermy intelligentsia crucifix vinyl literally tumblr poke bushwick readymade. Tacos sustainable nostrud humblebrag fam. Coloring book et deep v chillwave cornhole pitchfork air plant master cleanse fingerstache prism gluten-free laborum beard hammock. Affogato brooklyn cornhole salvia. Leggings slow-carb roof party fingerstache. Live-edge tempor thundercats truffaut lomo, cred shaman.',5),    
('fola', 1,'Cupcake ipsum dolor sit amet jelly gingerbread. Cookie apple pie tiramisu lollipop jujubes candy canes cheesecake I love macaroon. Bear claw jelly-o sugar plum jelly beans. Sweet roll sweet roll topping. Marzipan chocolate sesame snaps icing carrot cake cotton candy soufflé I love. Topping ice cream cotton candy macaroon I love brownie. Pudding I love icing caramels donut ice cream chocolate cake marzipan sesame snaps. I love I love powder jelly beans. Cookie gummies cotton candy candy sugar plum chocolate cake jelly beans gummi bears sweet roll. Lemon drops cake caramels liquorice cotton candy apple pie cupcake jujubes. Halvah carrot cake pie candy I love I love I love apple pie sweet roll. Pie pudding chupa chups jelly brownie powder sweet roll. I love donut gingerbread brownie candy canes I love I love powder.',5);