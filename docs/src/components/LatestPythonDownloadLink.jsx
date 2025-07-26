// src/components/LatestPythonDownload.js
import React, { useEffect, useState } from 'react';
import Link from '@docusaurus/Link';
import latestPythonReleaseVersionJson from '../../latest-python-release-version.json';

const LatestPythonDownload = () => {
    const [latestPythonReleaseVersion, setlatestPythonReleaseVersion] = useState(latestPythonReleaseVersionJson.latestPythonReleaseVersion);

    useEffect(() => {
        setlatestPythonReleaseVersion(latestPythonReleaseVersionJson.latestPythonReleaseVersion);
    }, [latestPythonReleaseVersionJson.latestPythonReleaseVersion]);

    const downloadUrl = `https://www.python.org/ftp/python/${latestPythonReleaseVersion}/python-${latestPythonReleaseVersion}-amd64.exe`;

    return (
        <Link href={downloadUrl} target="_blank" rel="noopener noreferrer">
            点我！我是 Python ({latestPythonReleaseVersion}) 下载链接。
        </Link>
    );
};

export default LatestPythonDownload;