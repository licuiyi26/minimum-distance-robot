# minimum-distance-robot
This is a CLI application to parse commands and display the result. Suppose a robot moves based on the commands it receives. And the commands tell the robot to move forward ("F") or backward ("B") in some units, and turn left ("L") or right ("R") at some times (only 90 degrees at a time), for example, "F1,R1,B2,L1,B3". <br>
<br>
<h3> Purpose </h3>
The purpose is to get the minimum amount of distance for a robot to get back to the starting point, which it must go in north, south, east, west directions only. <br>
<br>
<h3> How to Execute and Test the Code </h3>
* Download the robot.py to your IDE then run it! <br>
* Enter the commands by using a comma to separate them! (Notes: You can enter the commands in either lowercase or uppercase) <br>
* <i>OR</i> please go to the link here for live demo: https://trinket.io/python3/9c92c97579 <br>
<br>
<h3> Design Decision </h3>
* At the starting point, the robot is set to face <strong> NORTH </strong> by default.<br>
* The commands are split based on a comma; and if you enter any wrong commands, the robot will ignore them.<br>
<br>
<h3> Logic Behind It </h3>
* Firstly, check if the first command asks the robot to turn or move. <br>
* If it is to turn left or right, then the robot needs to turn into the dictated direction at corresponding times. Then the next command will tell the robot to move forward or backward.<br>
* Then if the first command tells the robot to move forward or backward, it will move to north or south in dictated units.<br>
