/*
This program will need to take in names of varying lengths. Among the list of names you must pick out only the friends.
Friends will always have exactly four letters in thier name!
*/

function friend(friends) {
  var friend = friends.filter(function(name) {
    return name.length == 4;
  });

  return friend;
}
console.log(friend(["Ryan", "Kieran", "Mark"]));
