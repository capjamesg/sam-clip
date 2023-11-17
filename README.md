# sam-clip

Use Grounding DINO, Segment Anything, and CLIP to label objects in images.

Below is an image with segmentation masks of all `McDonalds` logos in an image.

This demo was created by sending the prompt `logo` to Grounding DINO and SAM, then classifying each prediction using CLIP with two prompts: `McDonalds` and `Burger King`.

<img width="1051" alt="Screenshot 2023-11-17 at 09 41 44" src="https://github.com/capjamesg/sam-clip/assets/37276661/accde436-a33a-461b-a084-b9a65c8df785">

## License

This project is licensed under an [MIT license](LICENSE).
