# Project Ignite 2018 Video Game AI Group

This was a project done by Otis Smith, Jack Cameron, Will Aracri, Kyle Carskadden, Trey Natili, and Thomas Chang over a ten week period through Carnegie Mellon University's Project Ignite, with the assistance of Brian Scheuermann, Tiffany Ma, and Tyler Sikov. The project was presented at a showcase event at CMU in April, 2018.

The project was split into two main portions, programming an alpha-beta algorithm to play Connect 4, and using reinforcement learning to play simple simulations (CartPole and Pendulum) from OpenAI's Gym.

## Prerequisites

Before trying to run any of the files, make sure that Python 3, TensorFlow, and OpenAI Gym are all installed properly. See the individual product websites for each for installation instructions.

## Background on OpenAI Gym Simulations

Although much of this information can be found on [OpenAI Gym's website](https://gym.openai.com/docs/), it is worth explaining exactly what is going on. On the Gym website, there are many simple simulations, each of which are able to be run quickly and make collecting data for use with a neural network quite easy. Looking into the documentation reveals more information about how to access this information, which was implemented in the code. For this project, two simulations were used: CartPole and Pendulum. Each of these consists of a simple left/right input to the simulation, where the goal is to either balance a pole on a cart or to keep a spinning object upright for as much time as possible, respectively. The neural network acts in this scenario to maximize reward and minimize loss for the overall simulation.

## Using These Files

Given that much of the work relies solely on Python, TensorFlow, and Gym, little else is needed to run the files if these three are properly installed. Simply download the repository and run the .py files in the folder titled OpenAI_Gym_TensorFlow. Running these files anywhere will work, but running them in the command line shell outputs the data for epoch and loss best when the neural network is training.

The file named "CartPole.py" runs a few random input tests in a window, collects data, and trains a neural network based on those trials which scored well (according to the built in reward system in Gym). The second set of trials is the outputs generated by the neural network after it has been trained. Because the pole balances much better, the neural network was deemed successful in optimizing this situation.

The file named "pendulum.py" runs similarly, with the only difference being that the simulation is now the Pendulum simulation. The result after training is only marginally better, unfortunately, but does seem to have some improvement over random input. With more training time and adjustment of the neural network, results could likely be improved.

To use play against our Connect4 AI, go to the Alpha_Beta_Connect4 folder and open run_game.py (making sure that the other dependent files are present in the same folder). Uncomment the last line and then run the file. To play, click on the start game button, select which players you want to be human or AI and then press 'r' on the keyboard. Click within a column to drop a piece there.

## Built With

* [TensorFlow](https://www.tensorflow.org/) - The neural network Python library used
* [OpenAI Gym](https://gym.openai.com/docs/) - Simulations used

## Authors

* **Otis Smith** - *Worked on TensorFlow portion and writing README* - [themroats](https://github.com/themroats)
* **Jack Cameron** - *Worked on TensorFlow portion*
* **Will Aracri** - *Worked on Connect 4 portion, including writing estimator function for AI*
* **Kyle Carskadden** - *Worked on Connect 4 portion, including writing code for alpha beta AI*
* **Trey Natili** - *Worked on Connect 4 portion, including front end*
* **Thomas Chang** - *Worked on Connect 4 portion, including front end*

* **Brian Scheuermann** - *Advised project and wrote backend for Connect 4 game*
* **Tiffany Ma** - *Advised project, inclduing teaching Python graphics to Thomas and Trey and helping create the frontend*
* **Tyler Sikov** - *Advised project*


