import time
import sys


def display_celebration_animation():
    """Displays a short, dancing dog animation in the terminal."""
    
    # These are the different "frames" of our animation
    dog_frames = [
        "(>'.')>~",
        "~<('.'<)",
        "v( '.' )v",
        "^( '.' )^",
    ]
    
    # Animation parameters
    duration_seconds = 3  # How long the animation should last
    frames_per_second = 5 # How fast the animation plays

    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        for frame in dog_frames:
            # The '\r' moves the cursor to the start of the line
            output = f"\rSuccess! ✨ {frame} ✨"
            last_frame_length = len(output)
            
            sys.stdout.write(output)
            sys.stdout.flush()
            
            # The delay between frames
            time.sleep(1 / frames_per_second)
            
            # Check if total duration has been exceeded
            if time.time() - start_time > duration_seconds:
                break

    final_dog_pose = "<(^.^)> All done!"
    final_message = f"Success! ✨ {final_dog_pose} ✨"
    padding = " " * (last_frame_length - len(final_message) + 5)
    print(f"\r{final_message}{padding}")