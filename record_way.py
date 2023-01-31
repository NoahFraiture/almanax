from pynput.mouse import Controller, Button, Listener
from pynput import keyboard
import time
import normal_way
import scrap_alma_day


def record():
    steps = []

    def on_click(x, y, button, pressed):
        if pressed:
            match button:
                case Button.left:
                    steps.append((x, y, time.time()))
                case Button.right:
                    return False

    with Listener(on_click=on_click) as mouse_listener:
        mouse_listener.join()
    return steps

def go(steps):
    start_time = steps[0][2]
    m = Controller()
    b = Button.left
    for step in steps:
        time.sleep(step[2] - start_time)
        m.position = (step[0], step[1])
        m.press(b)
        m.release(b)
        start_time = step[2]
    return None

def main():
    instr = []

    def on_press(key):
        try:
            if 96 < key.vk <= 101:
                print(f"Go {key.vk - 96} times")
                for i in range(key.vk - 96):
                    print(f"Step {i+1} started")
                    _ = go(instr[-1])
                print("End step")
        except:
            pass

        match key:
            case keyboard.Key.delete:
                for i in range(4):
                    _ = go(instr[-1])

            case keyboard.Key.down:
                print("Starts record")
                instr.append(record())
                print("End record")

            case keyboard.Key.up:
                print("Start step")
                go(instr[-1])
                print("End step")

            case keyboard.Key.right:
                print("Start backward way")
                normal_way.backward()
                print("End backward way")

            case keyboard.Key.left:
                print("Start forward way")
                normal_way.forward()
                print("End forward way")

            case keyboard.Key.end:
                return False


    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    items = scrap_alma_day.getPage("https://www.krosmoz.com/fr/almanax")
    print("-"*50)
    print(f"Item of the Almanax : {items}")
    print("-"*50)
    print("Command :")
    print("Record : down")
    print("Go on : up")
    print("Go x times : number")
    print("Rigth click : end of record")
    main()