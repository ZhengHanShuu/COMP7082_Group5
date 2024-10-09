// scripts.js - JavaScript to enable editing and saving functionality

const editButton = document.getElementById('edit-button');
const saveButton = document.getElementById('save-button');

const weeklyGoalText = document.getElementById('weekly-goal-text');
const weeklyGoalInput = document.getElementById('weekly-goal-input');
const workoutFrequencyText = document.getElementById('workout-frequency-text');
const workoutFrequencyInput = document.getElementById('workout-frequency-input');

// Function to toggle display between text and input fields
function toggleEditMode(isEditable) {
    if (isEditable) {
        // Show inputs, hide texts and Edit button
        weeklyGoalText.style.display = 'none';
        weeklyGoalInput.style.display = 'block';
        workoutFrequencyText.style.display = 'none';
        workoutFrequencyInput.style.display = 'block';
        saveButton.style.display = 'block';
        editButton.style.display = 'none';
    } else {
        // Show texts, hide inputs and Save button
        weeklyGoalText.textContent = `Goal: Lose ${weeklyGoalInput.value} kg/week`;
        workoutFrequencyText.textContent = `Workout Frequency: ${workoutFrequencyInput.value} times/week`;

        weeklyGoalText.style.display = 'block';
        weeklyGoalInput.style.display = 'none';
        workoutFrequencyText.style.display = 'block';
        workoutFrequencyInput.style.display = 'none';
        saveButton.style.display = 'none';
        editButton.style.display = 'block';
    }
}


toggleEditMode(false);

// Enable editing when Edit button is clicked
editButton.addEventListener('click', () => {
    toggleEditMode(true);
});

// Save changes and switch back to text display when Save button is clicked
saveButton.addEventListener('click', () => {
    toggleEditMode(false);
});
