# Installation instructions

Author: Kris Thielemans

An easy way to run the exercises is to use the SIRF Virtual Machine where
SIRF has already been installed for you. Alternatively you can install SIRF yourself. Below are some brief instructions.

The exercises use [Jupyter notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html).
These provide a nice GUI interface to Python. You need 2 components:
the jupyter notebook server and a web browser.

## SIRF Virtual Machine

We distribute a VM with SIRF and all its dependencies, please [check our wiki](https://github.com/CCPPETMR/CCPPETMR_VM/wiki).
The VM also contains the source for the SIRF-Exercises. However, we do not include the data to restrict its file size.
Therefore, please install the VM as per the instructions, start it up, open a terminal and execute the following:

- We recommend first updating your VM

   update_VM.sh


- Get example data
   ```bash
    ~/devel/SIRF-Exercises/scripts/download_PET_data.sh
    ~/devel/SIRF-Exercises/scripts/download_MR_data.sh
   ```
   
  This will be a ~2.5 GB download.

  Note that if you want to run notebooks in MR/Old_notebooks (not recommended),
  you will have to get some more data
    ```bash
    ~/devel/SIRF-Exercises/scripts/download_MR_data_old_notebooks.sh
   ```

You now have everything ready.
 
Check our [README](README.md) for more information on usage.

## Installing SIRF and the exercises yourself

You will need SIRF of course. Please check the [instructions on our wiki](https://github.com/CCPPETMR/SIRF/wiki/How-to-obtain-SIRF).

The SIRF-exercises themselves can just be downloaded, preferably via

    mkdir ~/devel
    cd ~/devel
    git clone https://github.com/CCPPETMR/SIRF-Exercises


adjusting the path to where you want to install the SIRF-Exercises of course.

Finally, you need the jupyter server. Check first if your system comes with the jupyter server
by typing

    jupyter --help


If you need to install it, we currently recommend using `pip`. The following command
should work for you

    $SIRF_PYTHON_EXECUTABLE -m pip install jupyter

Note that we set an environment variable when you installed SIRF to make
sure that you use a Python version which is compatible with how you compiled SIRF.

Of course, if you've used (Ana)conda to install Python etc (and are sure
SIRF was compiled with that Python version), you can use conda to install
jupyter as well.

After all this, you will need to do the steps indicated in the instructions above for the VM.

### Updating the exercises after installation

You can repeat clone the repository again to get any updates. However, if you made any changes
to the exercises, you might want to keep those. Merging your changes and any
"upstream" ones is unfortunately a bit complicated
due to the file format used by jupyter notebooks. The following should work

    pip install --user nbstripout
    cd SIRF-Exercises
    nbstripout --install
    git config --global filter.nbstripout.extrakeys '
      metadata.celltoolbar 
      metadata.language_info.codemirror_mode.version
      metadata.language_info.pygments_lexer metadata.language_info.version'
    git pull

(You do not have to write the `nbstripout` lines on the VM, and on other systems you have to write those only once).
