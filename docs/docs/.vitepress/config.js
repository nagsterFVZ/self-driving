export default {
    title: 'Self Steering Vehicle',
    description: 'Documentation for the BeCreative self steering car project',
    themeConfig: {
        socialLinks: [
            { 
                icon: {
                    svg: '<svg style="width:24px;height:24px" viewBox="0 0 24 24"><path fill="currentColor" d="M19.5,2H4.5A2.5,2.5 0 0,0 2,4.5V19.5A2.5,2.5 0 0,0 4.5,22H19.5A2.5,2.5 0 0,0 22,19.5V4.5A2.5,2.5 0 0,0 19.5,2M10.7,17.2A1.2,1.2 0 0,1 9.5,18.4H5.8C5.14,18.4 4.6,17.86 4.6,17.2V5.8A1.2,1.2 0 0,1 5.8,4.6H9.5C10.16,4.6 10.7,5.14 10.7,5.8V17.2M19.4,12.2C19.4,12.86 18.86,13.4 18.2,13.4H14.5C13.84,13.4 13.3,12.86 13.3,12.2V5.8C13.3,5.14 13.84,4.6 14.5,4.6H18.2C18.86,4.6 19.4,5.14 19.4,5.8V12.2Z" /></svg>'
                }, 
                link: "https://trello.com/b/9ATMH1aF/project-management"
            },
            { icon: 'github', link: 'https://github.com/nagsterFVZ/self-driving' },
          ],
          nav: [
            { text: 'Project', link: '/project/' },
            { text: 'Files', link: '/files/' },
            { text: 'Blogs', link: '/blogs/' },
          ],
        sidebar: {
            '/project/': [
                {
                    text: 'Introduction',
                    items: [
                        { text: 'The Project', link: '/project/' },
                        { text: 'Parts', link: '/project/parts' },
                    ]
                },
                {
                    text: 'Research',
                    items: [
                    { text: 'Control System', link: '/project/research/control' },
                    ]
                },
                {
                    text: 'Installation',
                    items: [
                    { text: 'Introduction', link: '/project/-' },
                    { text: 'Research', link: '/project/-' },
                    ]
                },
            ],
            '/files/': [
                {
                    text: 'Vehicle',
                    items: [
                        // { text: 'The Project', link: '/files/' },
                    ]
                },
                {
                    text: 'Schematics',
                    items: [
                        // { text: 'The Project', link: '/files/' },
                    ]
                },
            ],
            '/blogs/': [
                {
                    text: 'Personal Blogs',
                    items: [
                        { text: 'Floris', link: '/blogs/floris' },
                        { text: 'Corné', link: '/blogs/corne' },
                        { text: 'Michael', link: '/blogs/michael' },
                        { text: 'Rane', link: '/blogs/rane' },
                        { text: 'Daan', link: '/blogs/daan' },
                        { text: 'Laurens', link: '/blogs/laurens' },
                        { text: 'Tom', link: '/blogs/tom' },
                    ]
                },
            ]
        }
    }
}
  