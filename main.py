import cv2
import blinkscript
import iris_position_estimation


def main():
    # Webcam
    # cap = cv2.VideoCapture(0)

    # Video with good lighting
    cap = cv2.VideoCapture('./vid/WIN_20230215_15_08_52_Pro.mp4')

    blinkscript.blink_counter(cap)
    iris_position_estimation.iris_position(cap)


if __name__ == '__main__':
    # asyncio.run(main())
    main()

    # Attempt to run both functions async
    # task1 = asyncio.create_task(blinkscript.blink_counter(cap))
    # task2 = asyncio.create_task(iris_position_estimation.iris_position(cap))
    #
    # # await both tasks to complete
    # await asyncio.gather(task1, task2)
