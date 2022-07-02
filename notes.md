MelGAN:
- Run without changes
- Create datasets for 
    - raining
    - forest
    - city
- Properly label datasets
    - Automate the process?
- Run with new datasets
- Run with new datasets with changes/albation
- Connect to Hex

Further Study:
Mean Opinion Score? (seems like it's designed for speech)
What can be done to improve long-form audio generation?



Dataset format:
MONO WAV
16 bit
22050Hz (or whatever, lower sample rates requires less computation)
TBC Duration (doesn't seem to matter a lot)
TBC Normallize (others don't do it)

venv name: melgan
create - `python3 -m venv melgan`
`source melgan/bin/activate`
`deactivate`

`ls *.wav | tail -n+10 > train_files.txt`
`ls *.wav | head -n10 > test_files.txt`

`python scripts/train.py --save_path logs/baseline --data_path wavs`

https://library.soundfield.com/browse/Ambience
https://github.com/descriptinc/melgan-neurips