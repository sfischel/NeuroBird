# NeuroBird
The NeuroBird: Using Steady-State Visually Evoked Potentials to Guide a Drone through an Obstacle Course


This project explores how distinct steady-state visually evoked potentials (SSVEPs) in the occipital lobe, induced by different frequencies of strobe lights, can be harnessed for drone flight control. Leveraging the variable brain response between viewing two separate screens of different strobing frequencies, we hope to develop an EEG-based interface for piloting a remote-controlled drone. When the user views a screen of some specific frequency, their brain activity displays a unique SSVEP related to that frequency, extractable as a feature in EEG data. The live EEG data measured through an OpenBCI Cyton Board would then interact with our DJI TelloDrone utilizing libraries PyTello for drone control, TensorFlow or PyTorch for signal processing, and NumPy for data manipulation.

In our implementation, a drone will move forward through a simple obstacle course, with a live video feed from its front camera streamed to the user in real time. The user will face two screens of different frequencies, where the left screen's strobe pattern corresponds to a leftward movement in the drone and the right screen's strobe pattern corresponds to a rightward movement. Presently, we are in the process of properly eliciting an identifiable response from the brain.

Our project is a proof of concept that SSVEP features in EEG data are sufficiently distinguishable by machine learning algorithms to be used in place of traditional tactile input methods.
