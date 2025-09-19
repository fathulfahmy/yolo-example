<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">YOLO Example</h3>

  <p align="center">
    A collection of computer vision applications using Ultralytics YOLO
    <br />
    <a href="https://github.com/fathulfahmy/yolo-example"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/fathulfahmy/yolo-example">View Demo</a>
    &middot;
    <a href="https://github.com/fathulfahmy/yolo-example/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/fathulfahmy/yolo-example/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This repository contains a collection of example applications using Ultralytics YOLO models for various computer vision tasks, including object detection, tracking, counting, region analysis, queue management, speed estimation, and workout monitoring.

### Features

- **Object Counting**: Count objects crossing a line or within a region.
- **Object Tracking**: Track multiple objects in real time.
- **Queue Management**: Monitor and analyze queues in video streams.
- **Region Counting**: Count objects within user-defined regions.
- **Segmentation Tracking**: Instance segmentation and tracking.
- **Speed Estimation**: Estimate the speed of moving objects.
- **Track Zone**: Track objects within specific zones.
- **Workout Monitoring**: Monitor workout movements using pose estimation.
- **Zone Tracking**: Track objects in a specific area or zone.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- Ultralytics
- OpenCV
- Numpy
- Python
- UV
- Ruff

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python >= 3.13

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/fathulfahmy/yolo-example.git
   ```
2. Install packages
   ```sh
   pip install .
   ```
3. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin fathulfahmy/yolo-example
   git remote -v
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Run the main menu to select an application:

```bash
python src/main.py
```

Or run any script directly, e.g.:

```bash
python src/object-counting.py
```

### Scripts

- `object-counting.py`: Count objects crossing a line or region.
- `object-tracking.py`: Track multiple objects in video.
- `queue-management.py`: Analyze and manage queues.
- `region-counting.py`: Count objects in user-defined regions.
- `segmentation-tracking.py`: Instance segmentation and tracking.
- `speed-estimation.py`: Estimate object speed.
- `track-zone.py`: Track objects in specific zones.
- `workout-monitoring.py`: Monitor workouts using pose estimation.
- `zone-tracking.py`: Track objects in a specific area.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/fathulfahmy/yolo-example/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the project
2. Create your feature branch (`git checkout -b feat/amazing-Feature`)
3. Commit your changes (`git commit -m 'feat: add some amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a pull request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/fathulfahmy/yolo-example/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=fathulfahmy/yolo-example" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Your Name - [@fathulfahmy](https://linkedin.com/in/fathulfahmy) - mfathulfahmy@gmail.com

Project Link: [https://github.com/fathulfahmy/yolo-example](https://github.com/fathulfahmy/yolo-example)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Ultralytics](https://docs.ultralytics.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
